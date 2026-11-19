# iOS 6 Faithful Edition — source review

This project has two separate categories of icon artwork:

1. **Public theme:** our own SVG interpretations, regenerated as SnowBoard PNGs. Safe source baseline and no copied raster assets.
2. **Local reference test:** exact historical icons that the device owner supplies from a personally downloaded icon archive. These files are not added to this repository, CI artifacts, the website, or a commercial release.

## The fork the owner provided

- Fork: https://github.com/Sentechtipsvn/iOS-6-Icons
- Upstream: https://github.com/zagnut531/iOS-6-Icons
- Original developer notes: icons manually extracted using iFile from an iPad 4 and an iPod touch 5. Includes independently made icons for apps released later.
- Checked top-level areas: `iPhone & iPod touch/Cropped icons`, `iPad/Cropped icons`, `Apple icons`, `3rd-party icons`.
- Exact file names and counts appear in `data/reference-inventory.json`.
- 34 application → source filename → Bundle ID mappings are in `data/reference-map.json`. **Bundle IDs remain unverified on the iPhone 7 Plus.**

### Rights assessment

Public GitHub and a successful fork do not prove a general license. The upstream project has **no standard LICENSE file** as inspected. Its README explicitly states Apple owns the first-party app icons and asks for credit to several community designers. These references are informative, not sufficient permission to redistribute a copy or sell it. The repo's MIT license covers only the code/art Sentechtipsvn owns, not external reference assets.

Other sources examined for study, not auto-import:
- https://github.com/pixdoet/ios6-icons — historic extracted iPad help assets; no license reported.
- https://github.com/lushm0nstera/Legacy-iOS-Themes — archived themes; no license reported.
- https://github.com/InstaTechHD/NostalgiaBoxRepo.github.io — historical APT packaging and theme metadata; no assertion of art license.
- https://github.com/ghaschel/iSketchbook — independently authored historic icon art, CC-BY-SA-4.0; attribution and share-alike obligations require reviewing before use.
- https://github.com/Disarto/disarto-icons — MIT icon artwork for alternative original designs, no transfer of third-party trademarks.

## Local-only visual evaluation (requires Python 3.11, Pillow, CairoSVG, dpkg-deb)

1. Download a copy of the **fork** as ZIP using GitHub (Code → Download ZIP) onto your own computer. Do not add its original images into this repo.
2. Run:
   ```bash
   python3 -m pip install -r requirements.txt
   python3 tools/generate.py
   python3 tools/import_local_references.py --source "/path/to/iOS-6-Icons-main.zip"
   sh scripts/package-local-reference.sh
   ```
3. The optional `dist-local/*.deb` is a separate **local-only test package**. It uses the theme title `iOS 6 Reference (Local)`, does not overwrite the public Sentech Retro 6 theme, and has a separate package ID.
4. Move that package privately to your own iPhone 7 Plus, install with Sileo, then select either theme in SnowBoard to compare. For public release use only independently owned/licensed assets.
5. Keep a copy of your current theme and disable/uninstall the test package to roll back.

**Security:** This workflow imports image files only. No SpringBoard hooks, MobileGestalt edits, or system audio replacements. It does not upload source photos/icons. The local ZIP may be quite large.

## Art direction after user feedback

Prioritize faithful **material and depth** rather than broadly applying a generic glossy overlay.

- Reference exact 2012-era icon silhouettes and the icon's own material: glass, metal, paper, leather, wood, sky, polished plastic.
- Build each artwork in layers: environmental lighting, embossed rim, material microtexture, central symbol, interior shadow, reflected highlight.
- Use iPhone rather than iPad cropped icons as the canonical iPhone 7 Plus reference.
- Keep app identity, avoid recreating brand logos for redistribution without sufficient rights, and keep modern-only apps (TikTok, Zalo) in a separately drawn, clearly inspired collection.
- Prefer higher-resolution layered master files for new custom icons; do not claim that enlarging a 114 px historic icon recreates missing detail.
- Document which app icons are static (Clock, Calendar) and which may require optional SnowBoard extensions. Test these separately.
- For every update verify theme activation, respring, badges, opening apps, third-party Bundle IDs, and rollback, recording SpringBoard Safe Mode incidents.

## Deployment status

- Alpha 0.1: verified installed on owner's jailbroken iPhone 7 Plus, icon theming functional; visual fidelity unsatisfactory.
- Faithful Edition source import tools: developed for evaluation, not yet tested on owner's device.
- GitHub Actions: public build remains original self-authored SVG assets only.
