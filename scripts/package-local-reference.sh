#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
theme="build/iOS 6 Reference Local.theme"
test -d "$theme/IconBundles" || { echo "Run tools/import_local_references.py first"; exit 1; }
command -v dpkg-deb >/dev/null || { echo "Missing dpkg-deb"; exit 1; }
stage="build/local-reference-stage"
rm -rf "$stage"
mkdir -p "$stage/DEBIAN" "$stage/var/jb/Library/Themes" dist-local
cp -R "$theme" "$stage/var/jb/Library/Themes/"
cat > "$stage/DEBIAN/control" <<'EOF'
Package: com.sentechtipsvn.retro6.reference-local
Name: iOS 6 Reference (Local Testing Only)
Version: 0.2.0-alpha.1
Architecture: iphoneos-arm64
Maintainer: Sentechtipsvn
Section: Themes
Priority: optional
Depends: com.spark.snowboard, firmware (>= 15.0), firmware (<< 16.0)
Description: Personal-use icon source comparison, not for redistribution.
Homepage: https://github.com/Sentechtipsvn/IOS6
EOF
chmod 755 "$stage/DEBIAN"
chmod 644 "$stage/DEBIAN/control"
dpkg-deb --build --root-owner-group "$stage" "dist-local/com.sentechtipsvn.retro6.reference-local_0.2.0-alpha.1_iphoneos-arm64.deb"
echo "LOCAL ONLY package ready. Not cleared for public distribution."
