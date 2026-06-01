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

- [ ] Add `mcpb/` build directory (kept out of the wheel; not in `tests/`)
- [ ] Author `mcpb/manifest.json` (manifest_version `0.3`, `server.type`
      `python`, `entry_point` `server/main.py`, `compatibility.platforms`
      `["win32"]`)
- [ ] Map env vars to `user_config` fields: `host` (required), `username`
      (default `admin`), `password` (`sensitive: true`), `screen_width`,
      `screen_height`, `use_https` (boolean), `verify_ssl` (boolean)
- [ ] Inject `user_config` into `mcp_config.env` as `NANOKVM_*` via
      `${user_config.KEY}`; set `PYTHONPATH` to `${__dirname}/server/lib`
- [ ] Add `server/main.py` thin entry that calls `nanokvm_mcp.server.main`
- [ ] Vendor Windows wheels into `server/lib/` via
      `pip install --target server/lib -r requirements.txt`
      (mcp, httpx, websockets, pycryptodome, pillow + pydantic deps)
- [ ] Declare `tools` array in manifest (16 `nanokvm_*` tools from server.py)
- [ ] Document the Python-runtime prerequisite (Claude Desktop ships Node,
      not Python); decide python vs `uv` server type and record rationale
- [ ] Validate with `npx @anthropic-ai/mcpb validate mcpb/manifest.json`
- [ ] Build with `npx @anthropic-ai/mcpb pack mcpb` → `nanokvm-mcp.mcpb`
- [ ] Manual install test in Claude Desktop on Windows; verify config form
      prompts and a tool call (e.g. `nanokvm_info`) succeeds
- [ ] Add bundle icon: copy `media/images.png` to `mcpb/icon.png` and
      reference it via the manifest `icon` field
- [ ] Update `README.md` with MCPB install instructions (English, §2)
