#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
test -d "build/Sentech Retro 6.theme/IconBundles" || { echo "Run python3 tools/generate.py first"; exit 1; }
command -v dpkg-deb >/dev/null
rm -rf stage
mkdir -p stage/DEBIAN stage/var/jb/Library/Themes dist
chmod g-s stage/DEBIAN 2>/dev/null || true
cp -R "build/Sentech Retro 6.theme" "stage/var/jb/Library/Themes/"
cat > stage/DEBIAN/control <<'EOF'
Package: com.sentechtipsvn.retro6.icons
Name: Sentech Retro 6 Icons (Alpha)
Version: 0.1.0-alpha.1
Architecture: iphoneos-arm64
Maintainer: Sentechtipsvn
Author: Sentechtipsvn
Section: Themes
Priority: optional
Depends: com.spark.snowboard, firmware (>= 15.0), firmware (<< 16.0)
Description: Original retro skeuomorphic SnowBoard icons on iOS 15 rootless. No executable hooks.
Homepage: https://github.com/Sentechtipsvn/IOS6
EOF
chmod 755 stage/DEBIAN
chmod g-s stage/DEBIAN 2>/dev/null || true
chmod 644 stage/DEBIAN/control
dpkg-deb --build --root-owner-group stage dist/com.sentechtipsvn.retro6.icons_0.1.0-alpha.1_iphoneos-arm64.deb
echo "Build only. iPhone installation not yet verified."
