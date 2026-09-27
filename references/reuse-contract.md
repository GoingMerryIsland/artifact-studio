# Existing component and style reuse contract

Apply this before modifying UI in an existing project. Keep the evidence brief for small changes, but never skip the gate. A visually similar replacement is a failed reuse result when an applicable source component exists.

## A. Establish the authoritative source before editing

1. Open the nearest working sibling page with comparable roles and density. Follow its imports/registrations to canonical exports, real definitions, styles and providers. Read at least one working usage for each component contract being reused; shared usage can cover several roles.
2. Resolve aliases, package exports and barrel re-exports. Search beyond conventional directories: shared, common, primitives, design-system, widgets, features, packages, templates, partials and custom registries. Inspect relevant Storybook/bootstrap config explicitly even if a discovery helper skips hidden paths.
3. Prefer the component actually used by current pages. Do not choose an obsolete, test, demo or third-party component solely because its name matches. If the app wraps a UI library, the app wrapper is the default contract.
4. Read root/layout/bootstrap and the style chain: resets, global CSS, component styles, CSS-in-JS caches/providers, theme attributes/classes, font loading, utilities and relevant content scanning/build configuration.
5. Map all requested visible roles, including unchanged inherited shell elements. Consolidate repeated roles without omitting variants. Include the existing caller and the new consuming expression/selector to make verification possible.

| Role / state | Canonical source + export/selector | Current working caller | Actual props/slots/events/variant | Planned consumer | Style/provider origin | Decision / gap evidence |
| --- | --- | --- | --- | --- | --- | --- |

Allowed decisions: reuse directly; compose existing pieces; extend a verified contract; new for a verified gap; explicit user-directed replacement. An unavailable runtime is not a verified gap in the design system. Search evidence for a gap should name searched paths/roles and why close candidates cannot fulfill it.

## B. Implement actual consumption

- Preserve import paths, module registration, selectors, template includes and inherited layouts appropriate to the framework. Trace aliases/re-exports to the real implementation.
- Import plus **render/use** the component. An unused import is not evidence. A locally shadowed symbol or look-alike selector is not the same component.
- Compose public APIs first. Do not copy component bodies/CSS into a preview, redefine Button/Card/Input locally, recreate an existing utility, or replace app components with raw controls to avoid dependencies.
- Preserve actual component variants and tokens. Do not invent props, copy hex values into a parallel theme, sprinkle arbitrary utility values, inject global resets, disable encapsulation, or use !important to approximate existing styling.
- Structural markup and genuinely new page layout may be new. Use established layout primitives/tokens where present and scope added rules. Keep existing consumers unchanged unless the request requires a shared change.
- Keep preview controls/fixture wrappers outside the product surface. Use canonical components even inside the fixture; mock only the service/data boundary needed for preview. Do not mock the UI component under test.
- With a missing dependency/provider, reproduce the real composition from the sibling/root before considering an adapter. Do not bypass authentication or weaken production guards. If execution is blocked, preserve native implementation and disclose the block.
- For required standalone export from an existing app, prefer the framework's build output, which retains reuse at source. If source sharing is impossible, label the result a reproduction and retain the requested native implementation; never call copied code direct reuse.

## Asset reuse when the UI needs media

- Search relevant public/static/assets folders, shared packages, icon components/sprites, asset manifests, CSS backgrounds, font declarations and current callers. Use the asset actually appropriate to the feature; do not force unrelated existing imagery into an empty slot.
- Inspect candidate images/SVGs visually when possible and check their role, content, dimensions, transparency and theme/locale variants. A filename match is only a candidate. For fonts inspect existing declarations, weights and loading; for animated/audio/video assets inspect the existing integration and fallback.
- Record role → canonical file/export/registered source → consumer → selected variant. Reuse the existing logo/icon/media wrapper or framework image component where the app supplies one, retaining its sizing, optimization, lazy-loading and accessibility contract.
- Reference original source paths or exports instead of creating renamed duplicates, tracing logos again, copying SVG paths into new components, changing the icon family, or recreating existing illustrations. Normal bundler output/copying into a requested portable build is allowed; retain source provenance and required attribution.
- Preserve aspect ratio, crop/object-position, transparency and responsive sizing appropriate to the existing use. Select the supplied dark/light logo variant rather than applying arbitrary recoloring. Keep CSS backgrounds and icon sprite references connected to the same asset sources.
- Use the project's existing asset delivery mechanism, including configured remote assets when that is the established source. Do not invent URLs, bypass access controls, leak signed URLs into reports or embed private credentials to make an asset load.
- If no suitable asset exists, document the searched locations and gap, then use a clearly identified placeholder or create/source an asset as the task permits. Do not claim a new/placeholder asset is original project media. Do not add unnecessary media solely to fill the page.
- Check the actual resolved request/import, successful decoding, correct variant, intrinsic dimensions and rendered crop when a browser is available. An HTTP 200 may be an HTML fallback rather than an image. Confirm font loading and avoid silent fallback fonts. Use meaningful alt text for informative images and empty alt for decorative images; do not treat accessibility text as a replacement for the requested asset.

## C. Verify component provenance and effective styles

Perform these checks on the final artifact, not only on the plan:

1. **Trace consumption:** requested route/story/harness → layout/provider → actual rendered usage → import/registration → canonical export/definition. Handle transitive composition: the parent may legitimately own the button, shell or font imports.
2. **Inspect diff:** locate new component definitions, raw replacements, class duplication, token overrides and dependency changes. Explain every new UI role. Unrelated primitive/theme changes and alternate design systems are defects.
3. **Trace effective styling:** entry/layout/bootstrap → style imports or links → theme scope → consumer. Check specificity/order and CSS module/scoped/shadow boundaries. Importing a stylesheet in an unused file cannot pass.
4. **Run the project:** use the native compiler/build or existing renderer/test utilities. Verify expected variants/props render and required providers are present. A successful static import search alone is insufficient runtime evidence.
5. **Compare browser state when available:** confirm fonts loaded, actual theme attribute/class, and representative computed font/color/background/border/radius/spacing values against a working source component under the same viewport/theme/state. Inspect hover/focus/disabled/loading if relevant. Mark this not verified when unavailable.
6. **Check shared-source propagation when useful:** in a disposable copy or test process, change one distinguishable source label/style token/variant and confirm the preview consumer reflects it; then discard the test change. Alternatively use source maps, renderer instrumentation or existing integration tests to establish actual execution. Do not alter the user's working source just to produce evidence. A propagation result proves linkage, not complete visual equality.

Keep separate statuses for source reuse, build/render, effective style loading and visual/interaction parity. A passing source gate cannot silently pass a missing browser gate. Do not invent a percentage or certify all frameworks based on one fixture.

## D. Concrete failures and correct responses

| Failure | Required correction |
| --- | --- |
| Button imported but a custom button is rendered | Render the real Button with its verified variant; remove the unused import and clone. |
| Correct component file name but obsolete source chosen | Trace the current sibling usage and use its canonical export. |
| Same colors copied into preview.css | Load the app token/theme source and reference it; remove shadowing copies. |
| Real component appears unstyled in isolated harness | Reproduce the bootstrap CSS/provider/font chain and CSS build configuration. |
| Vue component auto-registered without local import | Verify the actual registration resolver/config and rendered SFC name; do not force unnecessary manual imports. |
| Angular selector present without its component/module | Restore the real standalone imports/NgModule relationship and DI context. |
| React server boundary breaks in a client-only harness | Use a native route/story that respects the boundary; do not clone the UI into HTML. |
| Theme imported but absent on portal/shadow content | Restore the app's provider/root/portal token scope and verify computed styling there. |
| Source/project not accessible | Request the minimum missing source; label any authorized mockup as a reproduction. |

## E. Handoff

Summarize actual reuse: role → canonical source → consumer, inherited style/provider roots, reused asset sources/variants, necessary additions and their reason. Report build/render and browser evidence separately. For small changes this can be a few precise lines. Preserve detailed mapping with task evidence, not as extra product UI.
