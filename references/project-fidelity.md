# Project fidelity

## Inspect the connected source graph

Begin with the target route/component, layout, imports and working usages. Follow shared primitives, styling and providers until rendering is explainable. In workspaces inspect the target app and relevant shared packages; avoid reading every file or dependency/build folders.

Use targeted rg reads. The discovery helper skips symlinks, hidden configuration directories and build/dependency folders. Inspect explicitly relevant hidden configs separately. Its samples/ranges are not semantic analysis. If truncated, narrow to the target app or intentionally increase the bound; incomplete discovery cannot establish absence.

| Layer | Sources | Record |
| --- | --- | --- |
| Runtime | Manifests, installed dependencies, configs, entry points | App, version evidence, boundary, build/serve scripts |
| Routing | Routes, guards, layouts, loaders | Exact path, shell, navigation, deep links |
| Tokens | Global CSS, theme provider, modules, Tailwind CSS/config, Sass | Real token names/values, theme selector, specificity |
| Typography | Font declarations/loading, text components | Family, loaded weights, size/line height/tracking/wrapping |
| Components | Exports, stories, usages | Props/slots/events, variants, controlled state, loading/disabled |
| State/data | Providers, stores, services, hooks, validators | Shapes, ownership, effects, errors/loading |
| Assets | Icon modules, images, public path mapping | Actual import/path, size, aspect ratio, crop |
| Locale | Locale files, formatters, directionality | Copy keys, formats, long strings |

Record task-relevant evidence with source paths. Do not guess APIs from filenames or invent plausible token names. Separate dependency version ranges from resolved installed versions.

## Reuse ladder

1. Import the existing component with correct variants/providers.
2. Compose existing primitives.
3. Add a scoped variant/prop, preserving callers.
4. Extract a primitive only when repeated code justifies it.
5. Build new components only when needed, deriving their tokens and contracts from the system.

Use the mandatory reuse contract for existing projects. Standalone reproduction is a distinct output mode only when requested/authorized; copied or adapted code is not direct reuse and must be labeled accordingly. Runtime inconvenience alone never authorizes switching to reproduction. Screenshots cannot reveal validation, permissions or keyboard behavior: label assumptions.

## Appearance details

- Match max-width, margins, gutters, shell height, sidebar width and scroll containers.
- Load fonts before judging wrapping and alignment; match actual weights.
- Reuse spacing/control-height tokens; avoid arbitrary compensating margins.
- Preserve icon family, stroke, optical alignment, hit area and accessible names.
- Match media ratio, object-fit, clipping, radius and fallback. Respect fixed ratios such as 2:1.
- Inspect subtle borders in supported themes, sticky stacking, popovers/portals and modal backdrops.
- Preserve focus/hover/active/selected/disabled/error/loading styles, motion and reduced-motion behavior.
- Match responsive transformations: mobile navigation, stacking, overflow tables and disclosure instead of shrinking desktop.

## Missing or conflicting references

State which evidence exists: code, live app, screenshots, design file or brief. Resolve conflicts through explicit user intent. Ask only when the choice materially affects the target. Never claim an unseen source was analyzed or a screenshot reproduction reuses components it does not have.
