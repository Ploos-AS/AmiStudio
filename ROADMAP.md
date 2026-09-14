# AmiStudio roadmap

## M0 — Foundation

- [x] Define AmiStudio as an Amiga-specific RetroStudio consumer/backend.
- [x] Define initial machine profiles.
- [x] Define dependency boundary with RetroStudio.
- [x] Add minimal target descriptor fixture.
- [x] Add host-side checks and CI.
- [x] Document hardware-aware design goals.

Exit criterion: `make check` validates the repository, target profile data and RetroStudio API descriptor without requiring an Amiga SDK or emulator.

## M1 — Target profiles

- Machine profile parser/model.
- OCS/ECS/AGA capability flags.
- CPU, chipset and memory constraints.
- PAL/NTSC timing metadata.
- Stable diagnostics for invalid target settings.
- Tests for all baseline profiles.

## M2 — RetroStudio backend integration

- Implement RetroStudio target API negotiation.
- Backend discovery descriptor.
- Capability reporting.
- Structured target validation.
- Reference build/package hooks.

## M3 — Graphics asset pipeline

- PNG/source bitmap ingestion handoff.
- Palette quantization policy.
- Planar conversion.
- Tiles, masks and sprite conversion.
- OCS/ECS/AGA constraints and diagnostics.

## M4 — Audio asset pipeline

- Paula-compatible sample conversion.
- Sample-rate/size budgeting.
- MOD/module integration path.
- Target-aware audio diagnostics.

## M5 — 68k runtime foundation

- 68000 baseline runtime.
- 68020/AGA profile path.
- Input, timing, scene and entity runtime bridge.
- Deterministic runtime fixtures.

## M6 — Build and packaging

- m68k-amigaos toolchain integration.
- Executable output.
- ADF packaging.
- Hard-disk/WHDLoad-oriented layout.
- CD32 packaging foundation.

## M7 — Emulator workflow

- One-command build and launch.
- FS-UAE integration first.
- Optional Amiberry integration.
- Automated guest evidence where practical.

## M8 — Hardware-aware budgets

- Chip/Fast RAM accounting.
- Bitplane/palette/sprite budgets.
- Copper and blitter diagnostics.
- Frame-budget estimates.
- Audio/sample memory budget.

## M9 — AmiStudio product integration

- RetroStudio Linux editor integration.
- Amiga project wizard.
- Target inspector.
- Live hardware budget panels.
- Build/run/export UX.

## M10 — Release candidate

- Complete example games.
- Reproducible Linux packages.
- Documentation/tutorials.
- Real Amiga qualification matrix.
- v0.1.0 release.
