# AmiStudio

AmiStudio is the Amiga-focused frontend/backend for the RetroStudio game-development platform.

It provides Amiga target profiles, hardware-aware validation, asset conversion, runtime/build integration and emulator launch support while keeping generic editor and project logic in **RetroStudio**.

## M0 goals

- Define AmiStudio's boundary relative to RetroStudio.
- Establish initial Amiga target profiles.
- Add a minimal RetroStudio target descriptor.
- Add host-side checks and GitHub Actions CI.
- Document the roadmap toward a complete Linux-to-Amiga game-development workflow.

## Initial targets

- A500 / OCS / 68000
- A500+ / ECS / 68000
- A600 / ECS / 68000
- A1200 / AGA / 68020
- CD32 / AGA / 68020

Future optional performance profiles may include accelerated 020/030/040/060 systems, but the baseline engine must remain useful on original hardware.

## Architecture

```text
AmiStudio
  |
  +-- Amiga target profiles
  +-- graphics/audio conversion
  +-- hardware budgets/diagnostics
  +-- Amiga runtime/build backend
  +-- packaging and emulator integration
  |
  +--> RetroStudio Core
```

Generic scenes, entities, assets, scripting interfaces, build graphs and Linux editor infrastructure belong in RetroStudio.

See `docs/ARCHITECTURE.md`.

## M0 check

```sh
make check
```

No Amiga compiler, ROM or emulator is required for M0.

## Status

**M0 — Foundation:** implemented.

## License

MIT. See `LICENSE`.
