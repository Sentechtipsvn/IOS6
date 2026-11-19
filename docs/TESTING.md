# iPhone 7 Plus / iOS 15.8.8 — testing

Start with a **clean SnowBoard configuration** and record SnowBoard/Dopamine versions.

- [ ] Rootless Sileo installs the package without dependency error
- [ ] Theme appears under SnowBoard
- [ ] Phone, Safari, Messages, Settings, Photos and Camera show redesigned icons
- [ ] Apps open normally, Home Screen responds, notification badges remain readable
- [ ] Third-party apps are themed only if bundle IDs match installed versions
- [ ] No unexpected Safe Mode, crashes or spontaneous resprings
- [ ] Theme can be disabled without losing existing settings
- [ ] Uninstall restores original icons cleanly

**Rollback:** Settings > SnowBoard > disable Sentech Retro 6; remove the package in Sileo. Do not edit MobileGestalt or manually replace system files.

**Limitations:** No unlock/charging sounds, classic Dock UI, status bar, lock screen effects or animations in the alpha. These require separate opt-in modules after testing. No device runtime test has been performed yet.

For mismatched icons verify the exact Bundle ID in Filza/installed app bundle, then propose a correction in `data/apps.json`.