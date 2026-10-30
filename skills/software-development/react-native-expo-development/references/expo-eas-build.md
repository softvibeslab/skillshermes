# EAS Build Commands and Common Pitfalls

## Commands

- List builds: `eas build:list`
- Cancel a build: `eas build:cancel <build-id>`
- View build logs: `eas build:view <build-id>`
- Download artifacts: `eas build:download --platform android --latest` (or specify build-id)

## Common Pitfalls

1. **Missing credentials**: Ensure you have run `eas login` and that your account is linked to the project.
2. **Incorrect profile configuration**: Double-check `eas.json` for the build profile you are using (e.g., `preview`, `production`).
3. **Version and build code**: Remember to increment the version in `app.json` (or use `expo.version` and `expo.versionPolicy`) and the Android version code if required.
4. **Native modules and SDK version**: If you use custom native modules, ensure they are compatible with the Expo SDK version specified in `app.json`.
5. **Assets not included**: Make sure assets are referenced correctly and are present in the project. Use `expo export:web` or `expo prebuild` to verify.
6. **Environment variables**: For `EXPO_PUBLIC_*` variables, they must be declared in `app.json` under `extra.eas` or defined in the build profile env. They are injected at build time.
7. **Build fails on dependency**: Check the logs for npm/yarn errors. Sometimes clearing the cache (`npm cache clean --force`) or deleting `node_modules` and reinstalling helps.

## Example: Building an APK for internal distribution

```json
// eas.json
{
  "build": {
    "preview": {
      "android": {
        "buildType": "apk"
      },
      "env": {
        "EXPO_PUBLIC_SUPABASE_URL": "https://your-project.supabase.co",
        "EXPO_PUBLIC_SUPABASE_ANON_KEY": "your-anon-key"
      }
    }
  }
}
```

Then run:
```bash
eas build --platform android --profile preview
```