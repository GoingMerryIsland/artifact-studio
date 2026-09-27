# Quality gates

Record pass, fail, not verified or not applicable for each gate. Include route/state, command/action, observed outcome and evidence path. Explain not-applicable choices; unavailable checks cannot pass.

| Gate | Evidence |
| --- | --- |
| Component reuse | All in-scope roles mapped; actual rendered consumers import/register the canonical source. No no-op imports, copied implementations, bypassed app wrappers or unexplained replacements. Native render/build evidence where available. |
| Style inheritance | Root-to-consumer CSS/font/theme/provider chain traced and retained; no copied token palette or accidental overrides. Computed styles and representative states compared when a browser is available; otherwise mark visual application not verified. |
| Asset reuse | Applicable logos/icons/images/fonts/media traced to suitable existing sources and actual consumers; correct theme/locale variants, aspect ratios and wrapper APIs retained. Resolve/decode/load checks where available; necessary new assets or placeholders disclosed. |
| Runtime | Correct visible page; no new blocking compilation, console, hydration or asset errors. |
| Functionality | In-scope controls work and primary journey completes with relevant validation/failure states. |
| Visual | Image inspection under matching conditions; geometry, typography, spacing and details checked. |
| Responsive | Wide/mobile/breakpoint-boundary inspection; no accidental clipping/overlap/overflow. |
| Accessibility | Keyboard task, visible focus, labels, semantics, dialog focus/escape/return and readable contrast where affected. |
| Regression | Relevant existing checks and affected neighboring components; pre-existing failures separated. |
| Implementation parity | Preview and target app consume the same native UI source; fixtures/adapters are separate. Where runnable, compare target route and preview under matching conditions, including relevant production build behavior. Unavailable integration/visual checks stay not verified. |
| Preview | Actual link renders the artifact, not login/fallback; reachability/lifetime stated accurately. |

## Interaction checks

- Buttons/links: intended action/navigation, accessible name, loading/disabled state, no duplicate submit.
- Forms: labels, required/invalid input, helpful errors, preserved values, pending and success/failure feedback.
- Modals/drawers: open/close, appropriate Escape, focus containment/return, background scroll, mobile sizing.
- Search/filter/sort: correct matching/order, reset, empty results, counters and pagination reset.
- Tables/lists: long text, actions, boundaries, selection consistency and narrow layout.
- Tabs/menus: state/content association, keyboard operation, stacking and clipping.
- Upload/export: valid/invalid files, preview/reset and actual output when in scope; no fake success.
- Theme/locale: actual switching, hydration/persistence as applicable, long translations and formats.
- Data: disclose fixtures versus verified real API; exercise failures without mutating production.

Apply only checks relevant to the artifact; do not invent extra features to fill the matrix.

## Visual protocol

Match viewport, zoom/device scale, theme, locale, font readiness and fixture data. Capture full page and useful detail/transient states. View screenshots as images; file existence alone proves nothing.

Compare shell/geometry first, then typography/wrapping, spacing/alignment, colors/borders/shadows, icons/assets and interaction states. Distinguish measured observations from estimates. Do not invent similarity percentages. Pixel diffs help only with controlled conditions and require human/agent visual interpretation; anti-aliasing adds noise and matching pixels do not establish working UX.

Use the app's breakpoints. With none known start near 390px mobile and 1440px desktop, then a layout-transition width. Check hit areas and intentional table scroll separately from document overflow. Test requested browser engines; Chromium alone cannot prove all-browser compatibility.

## Repair and exit

Blocker: blank/wrong page, broken main flow, destructive action, secret exposure or inaccessible primary action.
Major: available source component bypassed, copied styling replacing the app theme, unresolved style/provider chain, wrong layout/contract, materially wrong typography, absent state, broken mobile navigation, keyboard trap or missing assets.
Minor: visible non-blocking alignment/spacing/color/motion mismatch.

Track reproduction → source cause → smallest fix → observed recheck. Address fixable in-scope blockers/majors, then visible polish. After two unsuccessful distinct fixes, gather new root-cause evidence instead of repeating. Report missing inputs/runtime honestly. Stop once applicable gates pass and a final review introduces no new material defects; avoid arbitrary extra rounds or architectural rewrites.

## Evidence record

```text
Artifact: requested route/component
Mapping: actual source/export → role
Preview: actual URL; local/managed/hosted; lifetime
Conditions: framework version evidence, viewport, theme, locale, fixtures
Gate: pass/fail/not verified/not applicable
Check: actual command/action + observed result + screenshot/log path
Correction: defect → fix → recheck
Limitations: simulated dependencies, unavailable checks, missing references
```

Keep detailed logs with the task; avoid credentials/private data in evidence. Summarize actual validation in the final response.
