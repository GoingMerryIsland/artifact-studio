---
name: artifact-studio
description: Build project-faithful interactive artifacts, components, screens, and prototypes with a verified browser preview. Use for Claude-style artifacts, index.html previews, component playgrounds, or UI implementation matching an existing app. Require evidence of actual reuse of existing components and loaded styles, rather than look-alike replacements. Analyze components, tokens, assets, providers, routes, and behaviors across Next.js, React, Vue, Nuxt, Angular, Svelte, Astro, HTML/CSS/JS, and other inspectable web stacks. Includes responsive, accessibility, functional, and visual verification with evidence-driven repair. Exclude document-only artifacts, native mobile execution, and unrelated backend-only changes.
---

# Artifact Studio

Deliver a working artifact that belongs to the actual application, plus a usable browser preview. Treat visual fidelity, interaction fidelity, and verifiable delivery as separate requirements. Never promise perfection, universal runtime support, an exact similarity percentage, or superiority to another tool without comparative evidence.

## 1. Establish scope and capabilities

1. Read the request and applicable project instructions. Identify the requested screen/component, project root, references, permitted changes, and audience.
2. Inspect the existing project before choosing a framework or drawing a UI. For a monorepo, select the target app and relevant shared packages; the root package need not be the app.
3. If source access is missing, request the project/path or minimum files needed for exact reuse. Meanwhile analyze available screenshots/briefs and do useful work without claiming repository fidelity. If standalone creation is authorized, label it an interpretation.
4. Check available shell, package manager, browser, screenshots, forwarding and hosting. A skill does not install an artifact panel, browser engine, runtime or hosting service.
5. Preserve existing changes. Do not upgrade frameworks, overwrite lockfiles, replace the design system or refactor unrelated code merely to simplify a preview.

Use the user's language for updates/handoff. Keep implementation notes outside the product UI unless it is a developer tool. Make routine choices autonomously; ask only when missing information materially changes correctness or access.

The existing-project reuse gate below is mandatory even for small tasks. For a small isolated change, follow the core workflow and load reference sections only to resolve a concrete uncertainty or failed gate. For a new screen, multi-route flow, provider/server integration or detailed reference matching, consult the relevant references before implementation. Keep all applicable checks; reduce reading overhead, not validation quality.

## 2. Analyze before implementation

Use targeted `rg --files` and `rg` reads. Optionally run this read-only discovery helper, replacing `SKILL_DIR` with this skill's directory:

```bash
python3 "SKILL_DIR/scripts/inspect_project.py" --root "/absolute/project"
```

Treat its output as candidates, not resolved versions, actual design tokens or runnable commands. Read the identified sources and inspect script bodies before executing them. Do not read secrets or dump environment values.

Inspect these connected layers:

- Runtime: manifests, lockfiles, package manager, installed framework versions, scripts, aliases, routing, SSR/CSR/static mode.
- UI foundation: global CSS, variables, Tailwind version/config or CSS theme, loaded fonts, reset, spacing, colors, borders/radii/shadows, breakpoints, density, motion and theme selectors.
- Components: requested component and imports, variants, props, slots, events, nearby usage, shared packages, icons/assets, stories, providers, stores, i18n and validation.
- Behavior: navigation, permissions, APIs, loading/error/empty/success states, responsive changes, persistence and keyboard interactions.

Consult [project-fidelity.md](references/project-fidelity.md) when mapping a larger source graph or matching detailed references. Keep a compact task-scoped evidence note in the project's review location or task scratch file:

| Requested area | Actual source/export | Props, tokens, behavior | Reuse decision | Evidence/uncertainty |
| --- | --- | --- | --- | --- |

Resolve conflicts using explicit user intent, then current authoritative project sources/runtime, then supplied visual references, then stated assumptions. If explicitly asked to match a screenshot that differs from code, follow the screenshot's appearance while preserving compatible contracts. Disclose meaningful deviations.

## Mandatory existing-project reuse gate

Before editing an existing app, read [reuse-contract.md](references/reuse-contract.md) and satisfy its preflight. This gate is not optional for a short task, isolated preview, screenshot request or missing runtime.

- Identify the current design system from a working sibling page and its source/registration chain. Search by role and usage across shared packages, widgets, primitives, templates and registries, not only folders named components/ui. A deprecated same-name component is not the authoritative one.
- Map **every in-scope visible UI role** to its existing source, real API/variant and intended consumer. Include shell, typography, buttons, inputs, cards, tables, overlays, feedback and icons where applicable. Record absence/search evidence for roles needing new implementations; do not omit them from the map.
- When an in-scope element needs a logo, icon, image, illustration, font or other media, inspect and reuse a suitable existing project asset first. Trace the actual asset registry/import/public path and current usage; preserve the intended light/dark, locale and responsive variant. Do not add stock/generated imagery, emoji substitutes, new icon packs or replacement fonts when a suitable source already exists. Follow the asset rules in the reuse contract.
- Trace style loading from the real root/layout/bootstrap: reset, theme/tokens, fonts, utility generation, component CSS and provider context. A CSS file found on disk is not proof that it applies to the preview.
- In the implementation, import/register/render the canonical components and load the established style chain. Keep actual variants, classes, slots, events, context and assets. A copied class string, unused import, cloned component, recreated stylesheet or renamed look-alike does not count as reuse.
- Never replace an available app wrapper with a raw element or the wrapper's underlying UI-library component just because that is easier. Plain semantic markup remains appropriate for structural elements that have no app abstraction. New components/styles require a documented gap, scoped extension or explicit user-directed replacement.
- Missing provider/backend/runtime is a setup problem: retain the original UI and solve its composition/adapters. If blocked, keep native source changes and mark execution unverified. Do not silently downgrade an existing app into standalone HTML or introduce a new UI kit.
- Reuse fidelity passes only after reviewing the actual consumer/import or registration chain, applicable style chain and diff for duplicates/overrides. Run native build/render and browser computed-style/state checks when available; otherwise state exactly which evidence is missing. Existing-source reuse and visual similarity are separate gates.

## 3. Select implementation and preview

Consult the matching section of [framework-adapters.md](references/framework-adapters.md) for framework-specific boundaries or preview decisions that are not already evident in the project.

| Situation | Preferred approach |
| --- | --- |
| Existing app/page/connected feature | Native implementation and a real route on its existing server. |
| Isolated component with an existing story/playground tool | Story/example using real components and provider decorators. |
| Isolated component without a playground | Scoped app route or small native harness; avoid shipping demo routes unintentionally. |
| Explicitly standalone client-only artifact with no existing app reuse requirement | HTML/CSS/JS with index.html when useful; local/bundled assets and HTTP preview. |
| Static deliverable needed | Existing supported static build after checking server features and deep links. |
| Backend unavailable | Explicit deterministic fixtures at a narrow adapter boundary; disclose simulation. |
| Unknown/non-JavaScript web stack | Inspect native manifests/templates/dev workflow and adapt without forcing React/Vite. |

Do not convert Next.js server components/actions, Nuxt SSR, Angular DI or backend templates into one HTML file for convenience. An HTML snapshot is not equivalent to a functioning app.

## 4. Implement with fidelity

1. Follow the recorded source mapping from the reuse gate. Reuse real imports/registrations, variants, tokens and providers; compose existing pieces before extending them. Read the canonical component and one working caller before choosing its API. Do not modify shared primitives solely to make the artifact easier.
2. Match typography/wrapping, dimensions, layout, shell geometry, alignment, icon size/stroke, image ratio/crop, border contrast and interaction states.
3. Preserve framework idioms, routing, state ownership, localization, validation and server/client boundaries. Avoid adding a second styling or state library without a concrete need.
4. Give every in-scope visible control an observable intended result: real filtering/sorting/pagination, form validation, modal dismissal/focus return and coherent navigation. Avoid decorative fake controls and blanket `href="#"` links.
5. Use realistic synthetic fixtures with stable identifiers; cover relevant empty, long-text, missing-image, error, pending and success states. Update counters/lists consistently.
6. Isolate demo fixtures and API adapters from production. Do not bypass real authentication, hardcode credentials or mutate live data/send payments/emails to demonstrate a flow.
7. Preserve the app's aesthetic. Do not add unrelated gradients, fonts, illustrations, icons or decorative cards when fidelity is the goal.
8. For a new design, define a small cohesive token system and reusable primitives first, then implement with the selected framework.

## Preview and implementation must share one UI source

For artifacts intended for an existing website, make the preview render the same native component files that the final app will consume. Keep layout, styles, assets, variants and provider composition shared with that app. Do not maintain a separate demo UI that must later be rewritten or translated from HTML into the production framework.

If a harness/story is necessary, keep it a thin wrapper importing those exact components. Put sample data and environment adapters at the boundary, preserving real prop/data shapes; do not use preview-only CSS overrides or altered UI markup to make the demo look right. Deliver exact source entry points and the integration location so implementation reuses the reviewed code.

Verify integration parity through the actual app route as well as the isolated preview when both exist. Compare identical fixture data, state, theme, locale, browser engine/version, viewport, device scale, zoom, font readiness and motion state. Check both appearance and behavior, including inherited CSS, portals and responsive changes. When relevant and available, recheck the production build, since a dev-only preview does not establish built-output parity. Record and fix observed differences before calling the implementation verified.

Treat a request for “100% identical” as a fidelity target, never an automatic guarantee. Source reuse prevents duplicate implementations but does not prove rendered equality. Report the exact comparison conditions, checks and remaining differences; if the target app or browser is unavailable, state that implementation parity is not verified. A screenshot comparison cannot establish equivalence of all interactions or environments.

## 5. Run and verify preview

Consult [preview-delivery.md](references/preview-delivery.md) for managed/hosted delivery, access constraints or server troubleshooting.

- Use verified scripts, the correct working directory and package manager. Reuse an existing running preview only if it belongs to this task.
- Default to loopback. Bind to 0.0.0.0 only when an authorized managed preview requires it.
- Capture the actual URL, port, process/session handle, route and readiness. Do not assume the preferred port or kill unrelated processes.
- Verify the requested route, assets and a unique visible marker. HTTP 200 can be a login page, error overlay or generic SPA fallback.
- A remote container's localhost is not accessible on the user's computer. Use the environment's actual preview URL or authorized forwarding/hosting; never fabricate a link.
- Distinguish downloadable file, embedded preview, local server and published URL. Explain availability/lifetime accurately. Do not silently upload private code/data to obtain a public URL.
- Immediately before handoff, recheck the actual route and visible marker. If the task server stopped, restart your own process and verify again; do not deliver a dead link as active.
- Keep a promised preview running through handoff using the environment's supported session facility. If persistence is unavailable, explain and provide the exact start command/path.

## 6. Verify, repair, recheck

Use [quality-gates.md](references/quality-gates.md) for detailed acceptance criteria or uncertain coverage. Scope checks to the requested component/page/flow and affected integrations while satisfying the requested fidelity.

1. Establish an existing-app baseline when runnable: route, viewport, theme, locale, fixture state, screenshot and known errors.
2. Review source reuse and style loading using the final diff: reject unused imports, clones, bypassed wrappers, shadowed theme variables and replacement CSS. For an isolated preview, prove that a change in the canonical component/token is reflected by its consumer using a disposable copy or trace when practical; never mutate production for this check. Run relevant existing build/type/lint/tests. Do not claim unrun commands, disable rules to hide failures, or conflate pre-existing errors with regressions.
3. Open the preview in the available browser. Exercise the primary user journey, keyboard operation and applicable loading/error/empty states. Inspect console, network, hydration and assets.
4. Capture and view screenshots at wide, mobile and breakpoint-boundary sizes based on actual app breakpoints. Check light/dark if supported or requested.
5. Compare matching reference conditions, beginning with layout/typography and then details. Screenshot differences alone cannot approve behavior.
6. Track severity, reproduction, source cause, correction and recheck evidence. Fix blockers, major mismatches, then visible polish. Re-run the failed check plus impacted flow.
7. Finish after applicable gates pass and a final review reveals no new material defects. Avoid speculative redesigns. After two unsuccessful distinct fixes to the same defect, collect new root-cause evidence or surface the missing dependency instead of looping blindly.
8. Mark unavailable checks **not verified** and explain why. Missing evidence cannot count as a pass or a self-assigned 100/100 score.

Optionally use the local Playwright smoke helper when Node and installed Playwright are available:

```bash
node "SKILL_DIR/scripts/browser_smoke.mjs" --url "http://127.0.0.1:PORT/route" --expect "Unique visible heading" --project "/absolute/project" --out "/absolute/task-evidence"
```

It captures two viewports and common runtime/resource/layout defects. It does not certify accessibility, interaction correctness, resemblance or all-browser support. Inspect its report and images, then perform task-specific interactions. Follow required managed-browser instructions when that environment supplies the browser instead.

## 7. Deliver

Lead with the actual preview link if available. Include a concise source-to-consumer reuse summary and disclose each necessary new component/style/asset or unresolved reuse gap. Do not report a clone as reused. Briefly state what changed, which existing components/styles were reused, preview scope/lifetime, relevant source entry points, actual checks completed, simulated integrations and material limitations. Keep detailed evidence with the work. Follow the environment's saving rules. Do not claim production readiness, universal framework compatibility or exact parity without evidence.

## Portability

Keep Markdown and references portable; platform metadata is optional. In OpenCode a copied portable directory must be named `artifact-studio` with SKILL.md at its root under a supported skill directory. Confirm host discovery rules instead of inventing slash commands or autocomplete settings. Missing runtime/browser/hosting capabilities remain explicit limitations.

## Resources

- [reuse-contract.md](references/reuse-contract.md): mandatory component consumption, style inheritance and reuse acceptance for existing projects.
- [project-fidelity.md](references/project-fidelity.md): source mapping, component contracts and styling.
- [framework-adapters.md](references/framework-adapters.md): stack-specific implementation and preview.
- [preview-delivery.md](references/preview-delivery.md): local/managed/hosted preview and troubleshooting.
- [quality-gates.md](references/quality-gates.md): functional, visual, responsive and accessibility acceptance.
- `scripts/inspect_project.py`: bounded read-only discovery; no installs or script execution.
- `scripts/browser_smoke.mjs`: optional installed-Playwright screenshots and smoke report; no installs.
