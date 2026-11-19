# Sentech Retro 6

**Classic soul. Modern iOS.** Original iOS 6-inspired icon theme by **© Sentechtipsvn**.

**Alpha target:** iPhone 7 Plus, iOS 15.8.8, Dopamine rootless, SnowBoard. **Device installation has not yet been tested.**

## Version 0.1.0-alpha.1
- **23 original SVG icons**, including Apple apps and third-party icons.
- **46 SnowBoard-compatible PNGs** rendered reproducibly from source (`bundleID-large.png` + `bundleID.png`).
- **Rootless .deb installer** placing assets in `/var/jb/Library/Themes/Sentech Retro 6.theme`.
- No executable tweak, no direct system modification, no automatic respring.
- Bundle IDs for third-party apps must be verified on Sếp's device; some might not match installed variants.

## Build
Use Linux (or a CI environment) with Python 3.11, `dpkg-deb`:
```sh
pip install -r requirements.txt
python3 tools/generate.py
sh scripts/package.sh
```

Download built `.deb` from [Actions](https://github.com/Sentechtipsvn/IOS6/actions) after a successful workflow run. Workflow builds are **untested alpha**, not stable releases.

## Install, test and remove
1. Make sure Dopamine rootless, Sileo and a compatible version of [SnowBoard](https://sparkdev.me) are installed.
2. Install the downloaded .deb through Sileo/Filza.
3. Enable **Sentech Retro 6** in SnowBoard settings; apply/respring only when requested.
4. Inspect Phone, Messages, Safari, Camera, Photos, Settings, then third-party apps; capture screenshots.
5. To roll back, disable the theme in SnowBoard, uninstall package via Sileo, and respring if needed.

See [Device Test Checklist](docs/TESTING.md).

## Roadmap
| Stage | Scope | Current status |
|---|---|---|
| 0.1 | SVG/PNG icons + rootless theme | Source ready, hardware test pending |
| 0.2 | More icons + bundle ID corrections | Planned |
| 0.3 | Wallpaper / classic Dock aesthetic | Planned |
| 0.4 | Opt-in sound replacement | Requires engine compatibility proof |
| 0.5 | Lock-screen and UI effects | Research, safety gated |

**Music/lock/unlock/charging sounds are not included in the icon package.** No Apple-extracted artwork or audio is included. Theme is independent of Apple.

This repository is the authoritative source for new builds; do not confuse earlier local test packages with GitHub Actions output.
