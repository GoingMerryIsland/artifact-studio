# Preview delivery

| Kind | Use | Handoff |
| --- | --- | --- |
| Local HTTP | Agent/user on same computer | Tested localhost URL and command; requires running server. |
| Managed/forwarded | Remote workspace with advertised preview capability | Actual returned URL, access restrictions and lifetime. |
| Hosted app/build | Publishing requested/already authorized | Tested deployed URL, demo limitations and runtime requirements. |
| HTML/build file | Portable/static output requested | Entry and assets; state HTTP requirements. |
| Embedded surface | Host explicitly supports it | In-chat scope; not a standalone public URL. |

A filename is not deployment. A file link is not HTTP preview. Remote localhost is not accessible on the user's computer.

## Start and verify

1. Inspect instructions, scripts, dependency state, package manager and existing task processes.
2. Resolve app/workspace and route. Read scripts first: they can do more than start a server.
3. Use supported long-running session tools and loopback by default. Follow documented managed forwarding if it needs 0.0.0.0.
4. Wait with bounded requests/polling; capture actual port/URL. Never kill unrelated listeners.
5. Fetch target route, open in a browser and confirm unique visible content, theme and assets. Inspect redirects. HTTP 200 alone is insufficient.
6. Check direct entry/refresh and navigation, router base, host fallback and API proxy.
7. Preserve cwd, start command, route, session handle, environment variable names only and lifetime in task evidence.
8. Recheck the route and expected content immediately before handoff. Restart your own failed server when possible and verify the replacement; otherwise mark preview delivery incomplete and supply restart instructions instead of presenting the URL as live.

## Publication

Local preview is routine work. Public exposure needs authorization already present in the session or final approval if required by the environment. Prepare and validate the concrete result before that final approval; do not ask again for authorized work. Use existing hosting/workflow, including its applicable skill. Do not migrate projects to another host just to get a link.

Keep secrets/private fixtures out of client bundles. Avoid accidentally publishing demo routes/mocks. Never serve the entire private repo with a generic static server; use only the dedicated artifact/build directory.

## Troubleshooting

- Port busy: reuse only if it is the task's server; otherwise choose an available port.
- No response: inspect startup, cwd, binding, mapping and process liveness.
- 200 but blank/login/error: inspect DOM, URL, console, providers, route guards and missing config.
- Missing assets/fonts: check network paths, base/public conventions, aliases, MIME and bundler config.
- Hydration mismatch: inspect initial data/time/randomness, locale, theme and browser-only APIs; fix causes instead of suppressing warnings.
- Deep-link failure: check router base, rewrite/fallback and deployment mode.
- Browser unavailable or access refused: honor tool permissions; do not bypass the refusal with alternate proxies or exposure. Complete source/build checks and mark affected visual/interaction gates not verified. Report the specific blocker without claiming success.
- No remote forwarding/hosting: report that a remotely accessible link could not be made and give reproducible local startup; never invent URLs.

## Optional smoke helper

browser_smoke.mjs resolves installed Playwright from the target project or an explicitly supplied absolute --playwright module path. It does not install packages/browsers. Use --executable for an available browser binary if necessary. By default its initial URL is restricted to loopback HTTP(S); --allow-remote opts into an already authorized remote preview. This is a URL scope check, not a network sandbox: pages may load external resources.

Use a unique visible --expect marker and a fresh --out evidence directory. It writes smoke-report.json and two screenshots; reruns overwrite these files. It checks runtime errors, failed requests/HTTP responses, broken images and document overflow. It uses a fresh context per viewport and avoids writing request URLs/query strings, console text or response bodies. Inspect detailed errors locally with task-specific browser tools as needed.

Zero findings means only a smoke pass. It does not prove functionality, accessibility, theme fidelity or visual resemblance. Inspect screenshots and perform the required interaction/visual checks separately.
