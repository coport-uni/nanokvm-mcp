# NanoKVM MCP Server

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Firmware](https://img.shields.io/badge/NanoKVM%20firmware-v1.4.2%20tested-brightgreen.svg)](https://github.com/sipeed/NanoKVM/releases)

**Let an AI assistant (like Claude) take control of a real computer — move the mouse, type on the keyboard, press the power button, and see the screen — over the network.**

This project connects [Claude](https://claude.ai) to a small piece of hardware called a [Sipeed NanoKVM](https://github.com/sipeed/NanoKVM). Once set up, you can simply tell Claude things like *"open Chrome and go to naver.com"* and it will actually do it on the target machine.

> ✅ **Verified working:** this server was used to drive a real Windows PC — launching Chrome from the taskbar and loading naver.com — entirely through Claude. See [How it was tested](#how-it-was-tested).

---

## Never heard of "MCP" or "NanoKVM"? Start here.

You only need to understand two simple ideas.

### 🧠 What is MCP?

**MCP (Model Context Protocol)** is a standard way to give an AI assistant new abilities. Think of it like a USB port for AI: you plug in a "tool," and now the assistant can use it. This project is one such tool — it gives Claude the ability to control a computer remotely.

### 🔌 What is a NanoKVM?

A **NanoKVM** is an inexpensive little device that plugs into another computer's HDMI and USB ports. To that computer, the NanoKVM *pretends to be a monitor, a keyboard, and a mouse*. Over the network, it lets you:

- **See** the screen (even the BIOS / boot screen, before any OS loads)
- **Type and click** as if you were sitting right in front of it
- **Press the power/reset button** without physically touching the machine

It's the kind of thing used to manage servers, headless mini-PCs, or a computer in another room.

**Put them together:** NanoKVM gives you remote hands and eyes on a computer → this MCP server hands those controls to Claude → you just describe what you want in plain language.

---

## What you can ask Claude to do

Once it's running, you can say things like:

- *"Take a screenshot so I can see what's on screen."*
- *"Open Chrome and go to naver.com."*
- *"Type my username and press Enter."*
- *"Press Ctrl+Alt+Delete."*
- *"Is the machine powered on? If not, turn it on."*
- *"Mount the Ubuntu ISO so I can reinstall the OS."*

| Category | What it can do |
|----------|----------------|
| **🖥️ Screenshots** | Capture the current screen as an image |
| **⌨️ Keyboard** | Type text, send key combos (Ctrl+C, Alt+F4, …) |
| **🖱️ Mouse** | Move, click, scroll, tap at exact screen positions |
| **⚡ Power** | Power on/off, reset, force shutdown |
| **💿 ISO Mounting** | Mount/unmount disk images for remote OS installs |
| **📊 Status** | Power LED, HDD activity, HDMI signal, resolution |

---

## What you'll need

1. A **Sipeed NanoKVM** connected to the computer you want to control, and reachable on your network. *(This project is tested against NanoKVM firmware **v1.4.2**.)*
2. The NanoKVM's **address** (IP or hostname) and its **login** (default is `admin` / `admin`).
3. **Python 3.10 or newer** on your own machine.
4. **Claude Desktop** or **Claude Code** (this is what you'll talk to).

---

## Quick start

### 1. Install the server

```bash
git clone https://github.com/scgreenhalgh/nanokvm-mcp.git
cd nanokvm-mcp
pip install -e .
```

### 2. Find your NanoKVM's address

Open the NanoKVM's web page in a browser (e.g. `http://192.168.1.100`) to confirm it works and to check/set the username and password. If your NanoKVM uses a non-standard port, include it (e.g. `192.168.1.100:8080`).

### 3. Tell Claude about it

Add the block below to your Claude config file:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "nanokvm": {
      "command": "python",
      "args": ["-m", "nanokvm_mcp.server"],
      "env": {
        "NANOKVM_HOST": "192.168.1.100",
        "NANOKVM_USER": "admin",
        "NANOKVM_PASS": "admin",
        "NANOKVM_SCREEN_WIDTH": "1920",
        "NANOKVM_SCREEN_HEIGHT": "1080"
      }
    }
  }
}
```

> 🔐 **Security note:** this file contains your NanoKVM password in plain text. **Don't commit it to git or share it.** This repository's `.gitignore` already excludes a file named `claude_desktop_config.json` so you don't upload it by accident.

### 4. Restart Claude and try it

Restart Claude Desktop (or Claude Code), then ask:

> *"Take a screenshot of the NanoKVM."*

If you see the target machine's screen, you're done. 🎉

---

## Install as a one-click bundle (MCPB, Windows)

Instead of editing JSON by hand, you can install this server as an
**MCPB bundle** — a single `.mcpb` file that Claude Desktop installs in
one click and that prompts you for the connection settings through a
form. This packaging targets **Windows** and runs on your system Python.

### Prerequisites

- **Windows** (the bundle vendors Windows-only binary wheels).
- **Python 3.10+** on your `PATH` (Claude Desktop ships Node, not Python,
  so the bundle relies on your system interpreter).

### Build the bundle

The vendored dependencies and the `.mcpb` file are build artifacts and
are not committed to git. Regenerate them from a clone:

```powershell
git clone https://github.com/coport-uni/nanokvm-mcp.git
cd nanokvm-mcp
.\mcpb\build.ps1
```

This produces `nanokvm-mcp.mcpb` in the project root.

### Install it

1. Open **Claude Desktop → Settings → Extensions**.
2. Drag `nanokvm-mcp.mcpb` onto the window (or use *Install from file*).
3. Fill in the configuration form — at minimum the **NanoKVM Host**, plus
   username, password, and screen size as needed. The password is stored
   securely and never written to a plain-text config file.
4. Enable the extension. Claude can now control the NanoKVM.

The form fields map to the same settings as the environment variables in
the [Configuration reference](#configuration-reference) below.

---

## Configuration reference

### Environment variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `NANOKVM_HOST` | **Yes** | – | NanoKVM address. Add `:port` if not on the default port |
| `NANOKVM_USER` | No | `admin` | Web UI username |
| `NANOKVM_PASS` | No | `admin` | Web UI password |
| `NANOKVM_SCREEN_WIDTH` | No | `1920` | Target screen width in pixels |
| `NANOKVM_SCREEN_HEIGHT` | No | `1080` | Target screen height in pixels |
| `NANOKVM_HTTPS` | No | `false` | Use HTTPS/WSS instead of HTTP/WS |
| `NANOKVM_VERIFY_SSL` | No | `true` | Set `false` for self-signed certificates |

> The screen width/height must match the target's actual resolution, because mouse clicks are positioned using these numbers.

### Claude Code (minimal)

```json
{
  "mcpServers": {
    "nanokvm": {
      "command": "python",
      "args": ["-m", "nanokvm_mcp.server"],
      "env": { "NANOKVM_HOST": "192.168.1.100" }
    }
  }
}
```

---

## Available MCP tools

These are the individual actions Claude can call. You normally won't call them by hand — you just describe what you want — but here's the full list.

### Power

| Tool | Parameters | Description |
|------|------------|-------------|
| `nanokvm_power` | `action`: `power`, `power_long`, `reset` | Power button / reset |
| `nanokvm_power_cycle` | `off_duration_ms` | Force off, wait, power on (good for machines with no reset, e.g. Raspberry Pi 5) |
| `nanokvm_led_status` | – | Power and HDD LED states |

- `power` – short press (≈800 ms): normal power on/off
- `power_long` – long press (≈5000 ms): force power off
- `reset` – press the reset button

### Display

| Tool | Parameters | Description |
|------|------------|-------------|
| `nanokvm_screenshot` | – | Capture the screen as a JPEG image |
| `nanokvm_hdmi_status` | – | HDMI connection state and resolution |
| `nanokvm_hdmi_reset` | – | Reset the HDMI capture |

### Keyboard

| Tool | Parameters | Description |
|------|------------|-------------|
| `nanokvm_send_text` | `text`, `language` | Type a string (up to 1024 characters) |
| `nanokvm_send_key` | `key`, `ctrl`, `shift`, `alt`, `meta` | Press one key, optionally with modifiers |

**Supported key names:** letters `a`–`z`, numbers `0`–`9`, function keys `f1`–`f12`, arrows `up`/`down`/`left`/`right`, navigation `home`/`end`/`pageup`/`pagedown`/`insert`/`delete`, and `enter`, `escape`, `tab`, `backspace`, `space`. Korean keyboards also have `hangul` (Han/English toggle) — see the [Korean input tip](#tip-typing-on-a-korean-windows-target).

### Mouse

| Tool | Parameters | Description |
|------|------------|-------------|
| `nanokvm_tap` | `x`, `y` | Tap (click) at a position |
| `nanokvm_click` | `button`, `x`, `y` | Click `left`/`right`/`middle`, optionally at a position |
| `nanokvm_move` | `x`, `y` | Move the cursor |
| `nanokvm_scroll` | `amount` | Scroll the wheel (positive = down) |

**Coordinates:** `(0, 0)` is the top-left corner; `x` grows to the right, `y` grows downward, in screen pixels based on `SCREEN_WIDTH`/`SCREEN_HEIGHT`. These are converted internally to the NanoKVM's 16-bit absolute range (1–32768).

### Storage & system

| Tool | Parameters | Description |
|------|------------|-------------|
| `nanokvm_list_images` | – | List available ISO images |
| `nanokvm_mount_iso` | `file`, `as_cdrom` | Mount an ISO |
| `nanokvm_unmount_iso` | – | Unmount the current ISO |
| `nanokvm_mounted_image` | – | Show the mounted image |
| `nanokvm_reset_hid` | – | Reset the virtual keyboard/mouse |
| `nanokvm_info` | – | NanoKVM device info |
| `nanokvm_hardware` | – | Hardware info |

### Tip: typing on a Korean Windows target

If the target PC's input is in Korean mode, typed Latin letters may turn into Hangul (e.g. `kvm` → `ㅏㅔㅡ`). Numbers and URLs in the browser address bar are usually fine, but if letters come out wrong, ask Claude to **press the `hangul` key once to switch to English** and try again.

---

## Use it from Python (optional)

You don't have to use Claude — the underlying client is a plain Python library:

```python
import asyncio
from nanokvm_mcp import NanoKVMClient

async def main():
    client = NanoKVMClient(
        host="192.168.1.100",
        username="admin",
        password="admin",
        screen_width=1920,
        screen_height=1080,
    )
    try:
        # See the screen
        png = await client.screenshot()
        with open("screenshot.jpg", "wb") as f:
            f.write(png)

        # Type and press Enter
        await client.paste_text("Hello, World!")
        await client.send_key("enter")

        # Move the mouse and click
        await client.mouse_move(960, 540)
        await client.mouse_click("left", 500, 300)
    finally:
        await client.close()

asyncio.run(main())
```

---

## How it works

```
┌─────────────────┐     HTTP / WebSocket     ┌─────────────────┐
│   Claude        │◄────────────────────────►│    NanoKVM      │
│  (the AI)       │                          │                 │
└────────┬────────┘                          │  ┌───────────┐  │
         │  MCP                              │  │ REST API  │  │
┌────────▼────────┐                          │  ├───────────┤  │
│  nanokvm-mcp    │   power / ISO / login    │  │ WebSocket │  │
│     server      │   keyboard & mouse  ───► │  │  (HID)    │  │
│  (this project) │   screenshots            │  ├───────────┤  │
└─────────────────┘                          │  │  MJPEG    │  │
                                             │  │  stream   │  │
                                             │  └───────────┘  │
```

| Feature | How it's sent |
|---------|---------------|
| Login | REST `POST /api/auth/login` (AES-encrypted password) |
| Power / ISO | REST `POST /api/vm/...`, `/api/storage/...` |
| Bulk text typing | REST `POST /api/hid/paste` |
| Key presses & mouse | **Binary** WebSocket frames on `/api/ws` |
| Screenshots | A single frame parsed from the MJPEG stream |

**A note for the curious (and a bit of project history):** the keyboard and mouse are the trickiest part. The NanoKVM firmware expects each keyboard/mouse event as a small **binary** packet over a WebSocket — the first byte selects the channel (keyboard or mouse) and the rest is a raw USB HID report. An earlier version of this server mistakenly sent these as JSON *text*, which the firmware silently ignored — so clicking and typing did nothing. This was rewritten to send the correct binary frames (matching NanoKVM firmware **v1.4.2**), which is why mouse, keyboard, and scroll now work end to end.

### How it was tested

Beyond the automated test suite, the rewritten input layer was verified against a **real NanoKVM (firmware v1.4.2)** controlling a Windows PC:

- moved the cursor to specific coordinates and confirmed it visually,
- clicked the Chrome icon in the taskbar to bring the browser forward,
- focused the address bar (`Ctrl+L`), typed `naver.com`, pressed Enter, and
- confirmed the **Naver homepage fully loaded** — all driven through this server.

---

## Development

```bash
git clone https://github.com/scgreenhalgh/nanokvm-mcp.git
cd nanokvm-mcp
pip install -e ".[dev]"   # includes pytest, pytest-asyncio, etc.
pytest                    # run the test suite
```

### Project layout

```
nanokvm-mcp/
├── nanokvm_mcp/
│   ├── server.py   # MCP server + tool definitions (FastMCP)
│   ├── client.py   # NanoKVM client (REST + WebSocket HID + screenshots)
│   ├── auth.py     # AES password encryption (matches the web UI)
│   └── hid.py      # USB HID keycodes + binary report builders
├── tests/          # pytest suite
├── README.md
└── API_REFERENCE.md
```

For the full protocol details (endpoints, the exact binary HID layout, keycodes), see [API_REFERENCE.md](API_REFERENCE.md).

---

## Troubleshooting

**Can't connect / connection refused**
1. Ping the NanoKVM: `ping <NANOKVM_HOST>`.
2. Open its web UI in a browser: `http://<NANOKVM_HOST>`.
3. Double-check the host (and `:port` if non-standard) and credentials.

**Login fails**
1. Default credentials are `admin` / `admin`.
2. Confirm the password in the NanoKVM web UI.

**Mouse/keyboard does nothing**
1. Make sure your NanoKVM firmware is **v1.4.2** (older firmware may use a different input protocol). Check with the `nanokvm_info` tool.
2. Try the `nanokvm_reset_hid` tool, and confirm the USB cable to the target is connected.
3. Make sure you have a recent `websockets` package installed (`pip install -e .` handles this).

**Screenshot times out**
1. Ensure HDMI is connected and a signal is detected (`nanokvm_hdmi_status`).
2. Try `nanokvm_hdmi_reset`.

**Letters come out as Hangul** — see the [Korean input tip](#tip-typing-on-a-korean-windows-target).

---

## License

MIT

## Related projects

- [Sipeed NanoKVM](https://github.com/sipeed/NanoKVM) — the hardware this server controls
- [Model Context Protocol](https://modelcontextprotocol.io/) — the AI-tooling standard
- [FastMCP](https://gofastmcp.com/) — the Python MCP framework used here
