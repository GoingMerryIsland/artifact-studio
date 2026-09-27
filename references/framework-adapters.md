# Framework adapters

Use installed versions, actual config and project scripts as authority. These are strategies, not unconditional commands. Read scripts before execution and preserve the package manager. Do not install latest or generate a fresh app inside an existing app to obtain a preview.

Apply the mandatory reuse contract in every adapter. Resolve the real component consumption and effective style chain; framework recognition alone is not evidence of reuse.

## Next.js

Identify App/Pages Router, route groups/layouts, server/client boundaries, aliases and providers. Keep server data/secrets on the server; add the smallest client boundary. Use the real app for navigation context, server modules/actions, image/font handling and auth. Use existing dev/build/start scripts; development success does not prove a production build.

Trace layout/root CSS, font classes, CSS-module imports, theme and client providers through the actual route. Do not import a server component into a client-only playground or recreate it in JSX to bypass that boundary. If shadcn or another library is wrapped in local components, import the app-owned wrapper used by current pages.

Static export is optional and limited. Request-dependent features and server actions cannot be retained by simply setting output to export. Do not change app output mode just for artifact delivery. Isolate fixture adapters for backend-free demos and disclose simulation.

## React / Vue with Vite or another bundler

Reuse aliases, global CSS, plugins and bootstrap code. React must retain relevant router, query/state, theme and i18n providers. Vue must retain SFCs, scoped CSS, props/emits/slots, composables, Pinia/Vuex and plugin setup as applicable.

Use existing dev scripts; for built preview, build before running configured preview. Vite preview is a local build check, not production hosting. Verify base/public paths and SPA history fallback through actual deep-link refreshes.

For Vue auto-registration, inspect resolver/plugin config and actual component resolution; a missing explicit import can be valid. For Tailwind, retain the project version and content/source scanning paths, including workspace UI packages, so reused classes generate CSS. For CSS-in-JS, retain theme/cache/style injection context.

## Nuxt

Inspect version, auto imports, plugins, layouts, middleware, server routes, runtime config and rendering mode. Preserve SSR-compatible composables and hydration. Do not disable SSR just to hide a browser-only bug. Use native dev/built preview; static generation requires checking routes and backend features.

## Angular

Inspect angular.json/project config, target app, builder, standalone/NgModule conventions, router, providers and encapsulation. Preserve DI, inputs/outputs, existing signals/observable conventions, reactive forms and change detection. Use the configured serve target. Do not substitute React or HTML for Angular components. A story/harness needs correct providers, router and styles. Derive build output and client/server split from the actual builder/version.

For Angular, prove selector → component class → standalone import or NgModule export/import → route, plus required providers. Retain angular.json global styles and component styleUrls/styles; do not disable encapsulation to imitate appearance.

## Svelte / SvelteKit

Identify version, state conventions, layouts, load functions, actions and deployment adapter. Preserve scoped styles, reactivity and server/client module boundaries. Use existing scripts; choose static output only when route/server features permit it.

## Astro

Preserve layouts/content, integrations and island hydration directives. Avoid unnecessary full-page hydration. Inspect static/server rendering and adapters. Verify both initial rendering and hydrated interaction in the real setup.

## HTML / CSS / JavaScript

Use semantic HTML, project tokens and native controls. Modularize when one file becomes unwieldy. index.html can be the entry, but assets/modules/fetch often need HTTP. Claim file:// support only if tested. Serve a dedicated artifact/build folder, not the private repo root. Bundle assets if portability is requested. Avoid remote CDN dependencies for offline/self-contained output.

## Other stacks and native shells

For Laravel/Blade, Django, Rails, ASP.NET, web components, Solid, Qwik or an unfamiliar stack, inspect manifests/templates/assets/routes and native dev workflow. Adapt to evidence instead of forcing a rewrite; report unsupported/unverified features.

A Tauri/Electron browser preview can show its web UI with an explicit bridge adapter; IPC, device, filesystem and window behavior require the native runtime. Native mobile UI needs its own runtime: do not claim web reproduction executes native components.

## Official references

Consult version-specific docs only for unresolved behavior. References consulted 2026-09-21; project versions may differ.

- [Next.js static export](https://nextjs.org/docs/app/guides/static-exports)
- [Vite build preview/deployment](https://vite.dev/guide/static-deploy.html)
- [Angular development server](https://angular.dev/tools/cli/serve)
- [OpenCode skill discovery](https://opencode.ai/docs/skills/)
