#!/usr/bin/env python3
"""Bounded, read-only discovery. Does not execute scripts or read secret files."""
import argparse
import json
import os
from pathlib import Path

SKIP = {'node_modules', 'vendor', 'dist', 'build', 'out', 'coverage', '__pycache__', 'venv', 'target'}
LOCKS = {'pnpm-lock.yaml': 'pnpm', 'package-lock.json': 'npm', 'npm-shrinkwrap.json': 'npm',
         'yarn.lock': 'yarn', 'bun.lock': 'bun', 'bun.lockb': 'bun'}
FRAMEWORKS = {'next': 'Next.js', 'nuxt': 'Nuxt', '@angular/core': 'Angular',
              '@sveltejs/kit': 'SvelteKit', 'astro': 'Astro', 'react': 'React',
              'vue': 'Vue', 'svelte': 'Svelte', 'solid-js': 'Solid',
              '@builder.io/qwik': 'Qwik', 'vite': 'Vite', 'electron': 'Electron',
              '@tauri-apps/api': 'Tauri'}
STYLE = ('tailwind', 'sass', 'less', 'styled-components', '@emotion/', '@mui/',
         '@radix-ui/', '@heroui/', 'antd', 'vuetify', 'primevue', 'lucide', 'bootstrap')


def inspect(root, limit):
    manifests, paths, warnings = [], [], []
    truncated = False
    def walk_error(error):
        warnings.append({'path': str(Path(error.filename).relative_to(root)), 'issue': 'unreadable directory'})
    for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d not in SKIP
                         and not (Path(directory) / d).is_symlink())
        for name in sorted(files):
            file = Path(directory) / name
            if name.startswith('.') or file.is_symlink():
                continue
            if len(paths) >= limit:
                truncated = True
                break
            rel = file.relative_to(root).as_posix()
            paths.append(rel)
            if name != 'package.json':
                continue
            try:
                if file.stat().st_size > 1_000_000:
                    warnings.append({'path': rel, 'issue': 'manifest exceeds size limit'})
                    continue
                data = json.loads(file.read_text(encoding='utf-8-sig'))
                if not isinstance(data, dict):
                    raise ValueError('manifest must be object')
                deps = {}
                for field in ('dependencies', 'devDependencies', 'peerDependencies'):
                    if isinstance(data.get(field), dict):
                        deps.update({k: v for k, v in data[field].items() if isinstance(v, str)})
                scripts = data.get('scripts', {})
                manifests.append({
                    'path': rel,
                    'package_manager_declared': data.get('packageManager') if isinstance(data.get('packageManager'), str) else None,
                    'framework_candidates': [{'package': k, 'framework': v, 'declared_range': deps[k]}
                                             for k, v in FRAMEWORKS.items() if k in deps],
                    'style_dependencies': {k: v for k, v in deps.items() if any(t in k for t in STYLE)},
                    'script_names': sorted(scripts) if isinstance(scripts, dict) else [],
                    'has_workspaces': bool(data.get('workspaces')),
                })
            except (OSError, ValueError, UnicodeError):
                warnings.append({'path': rel, 'issue': 'unreadable or invalid manifest'})
        if truncated:
            break
    groups = {
        'lockfiles': [p for p in paths if Path(p).name in LOCKS],
        'workspace_configs': [p for p in paths if Path(p).name in ('pnpm-workspace.yaml', 'nx.json', 'turbo.json', 'lerna.json')],
        'config_candidates': [p for p in paths if Path(p).name.startswith(('next.config.', 'nuxt.config.', 'vite.config.', 'svelte.config.', 'astro.config.', 'tailwind.config.', 'tsconfig')) or Path(p).name == 'angular.json'],
        'style_candidates': [p for p in paths if Path(p).suffix.lower() in ('.css', '.scss', '.sass', '.less')],
        'component_candidates': [p for p in paths if (any(x in ('components', 'ui', 'shared', 'common', 'primitives', 'design-system', 'widgets', 'templates', 'partials') for x in Path(p).parts) or '.component.' in Path(p).name or Path(p).suffix.lower() in ('.vue', '.svelte')) and Path(p).suffix.lower() in ('.tsx', '.jsx', '.vue', '.svelte', '.ts', '.js', '.mjs', '.html', '.php', '.astro')],
        'source_candidates': [p for p in paths if Path(p).suffix.lower() in ('.tsx', '.jsx', '.vue', '.svelte', '.astro', '.ts', '.js', '.mjs', '.html', '.php', '.erb', '.cshtml')],
        'bootstrap_and_style_config_candidates': [p for p in paths if Path(p).stem.lower() in ('main', 'app', 'layout', '_app', 'providers', 'theme', 'tokens', 'index', 'bootstrap', 'app.config', 'app.module') or Path(p).name.startswith(('tailwind.config.', 'postcss.config.'))],
        'registry_candidates': [p for p in paths if Path(p).name in ('components.json', 'components.d.ts', 'auto-imports.d.ts', 'angular.json') or any(t in Path(p).name.lower() for t in ('registry', 'resolver', 'plugin'))],
        'story_candidates': [p for p in paths if '.stories.' in Path(p).name],
        'asset_candidates': [p for p in paths if Path(p).suffix.lower() in ('.svg', '.png', '.jpg', '.jpeg', '.webp', '.woff', '.woff2')],
        'other_stack_manifests': [p for p in paths if Path(p).name in ('composer.json', 'Gemfile', 'pyproject.toml', 'requirements.txt', 'Cargo.toml', 'deno.json', 'deno.jsonc') or Path(p).suffix == '.csproj'],
    }
    lock_managers = sorted({LOCKS[Path(p).name] for p in groups['lockfiles']})
    return {'root': str(root), 'scanned_files': len(paths), 'truncated': truncated,
            'manifests': manifests, 'lockfile_manager_candidates': lock_managers,
            'candidates': {k: {'count': len(v), 'sample': v[:50]} for k, v in groups.items()},
            'warnings': warnings,
            'limitations': ['Path candidates require source/consumer inspection; no import graph or actual reuse is proven, and no scripts were executed.',
                            'Dependency ranges are not installed versions. Script bodies are intentionally omitted.',
                            'Symlinks, hidden files/directories and common build/dependency folders are skipped.',
                            'Multiple lockfiles may belong to different workspace apps; do not guess a global manager.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--max-files', type=int, default=12000)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        parser.error('--root must be an existing directory')
    if args.max_files < 1:
        parser.error('--max-files must be positive')
    print(json.dumps(inspect(root, args.max_files), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
