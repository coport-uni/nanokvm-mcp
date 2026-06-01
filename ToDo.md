# ToDo

Cumulative command history for Claude Code sessions (see `CLAUDE.md` §4 Task
Management). Append-only: never overwrite, reorder, or delete past entries.
Only checkbox state and a trailing commit/issue link may be updated.

---

## 2026-06-01 | Adopt CommonClaude conventions

- [x] Fetch `CLAUDE.md` from coport-uni/CommonClaude
- [x] Create `CLAUDE.md` in repo root with the convention ruleset (§1–17, English)
- [x] Create `claude_test/` scratch area with `README.md` index
- [x] Create `ToDo.md` (this file)
- [x] Add `[tool.ruff]` config (`line-length = 80`) to `pyproject.toml`
- [x] Add `.ruff_cache/` to `.gitignore`

## 2026-06-01 | Apply linting & pre-commit scaffolding

- [x] Add `.pre-commit-config.yaml` (§16)
- [x] Run `ruff check` / `ruff format` on `nanokvm_mcp/` and `tests/` (§6) — all checks passed, 11 files formatted
- [x] Fix or report remaining lint issues — 10 fixed (7 auto F401, 3 manual F841 unused `result` in test_client.py)

## 2026-06-01 | Package as MCPB bundle (Windows-only)

Goal: produce a one-click-installable `.mcpb` bundle of `nanokvm-mcp`
for Claude Desktop on Windows. Manifest spec version 0.3.

- [x] Add `mcpb/` build directory (kept out of the wheel; not in `tests/`)
- [x] Author `mcpb/manifest.json` — used manifest_version `0.4` (latest
      example), `server.type python`, `compatibility.platforms ["win32"]`
- [x] Map env vars to `user_config` fields: `host` (required), `username`
      (default `admin`), `password` (`sensitive: true`), `screen_width`,
      `screen_height`, `use_https` (boolean), `verify_ssl` (boolean)
- [x] Inject `user_config` into `mcp_config.env` as `NANOKVM_*` via
      `${user_config.KEY}`; set `PYTHONPATH` to `${__dirname}/server/lib`
- [x] Add `server/main.py` thin entry that calls `nanokvm_mcp.server.main`
- [x] Vendor Windows wheels into `server/lib/` via
      `pip install --target` (installs the project + deps; 80 MB, 104 .pyd)
- [x] Declare `tools` array in manifest — 19 `nanokvm_*` tools (not 16)
- [x] Decided `python` server type (system Python) over `uv`; documented
      the Python-runtime prerequisite in the README
- [x] Validate with `npx @anthropic-ai/mcpb validate` — schema passes
- [x] Build with `npx @anthropic-ai/mcpb pack mcpb` → `nanokvm-mcp.mcpb`
      (34 MB packed; verified archive root layout)
- [ ] Manual install test in Claude Desktop on Windows (deferred to user —
      requires a GUI session)
- [x] Add bundle icon: copied `media/images.png` to `mcpb/icon.png`,
      referenced via manifest `icon` field
- [x] Update `README.md` with MCPB install instructions (English, §2)

Issue coport-uni/nanokvm-mcp#1 · PR coport-uni/nanokvm-mcp#2 ·
branch `feature/mcpb-packaging`. Added `mcpb/build.ps1` (reproducible
build) and ignored `*.mcpb`. Remaining: live Claude Desktop install
test on Windows (user to verify).
