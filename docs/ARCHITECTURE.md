# AmiStudio architecture

## Role

AmiStudio is an Amiga-specific product/backend built on RetroStudio. It must not fork or duplicate RetroStudio's generic project/editor logic.

## Responsibilities

AmiStudio owns:

- Amiga machine/target profiles;
- OCS/ECS/AGA capability descriptions;
- planar graphics and palette conversion;
- sprite/copper/blitter-aware validation and budgeting;
- Paula-oriented audio conversion/runtime integration;
- Amiga compiler/linker/runtime integration;
- packaging for executable, disk and CD-oriented targets;
- FS-UAE/Amiberry launch integration;
- target-specific diagnostics.

RetroStudio owns:

- generic project and scene models;
- entities/components and scripting contracts;
- source asset registration;
- generic build graph and diagnostics transport;
- Linux editor infrastructure;
- backend discovery and API negotiation.

## Dependency rule

AmiStudio may depend on RetroStudio. RetroStudio must never depend on AmiStudio.

## Initial target IDs

- `amiga-a500-ocs`
- `amiga-a500plus-ecs`
- `amiga-a600-ecs`
- `amiga-a1200-aga`
- `amiga-cd32-aga`

Target IDs are stable machine profiles, not marketing aliases. Future accelerated profiles should be additive.

## Hardware-aware development

The long-term objective is not merely to compile a generic game to 68k. AmiStudio should expose meaningful resource budgets and constraints while the game is authored, including chip RAM, fast RAM, bitplanes, palette limits, sprite use, copper complexity, blitter load, audio/sample memory and frame-time estimates.

## M0 non-goals

- production graphics/audio conversion;
- real 68k compilation;
- FS-UAE runtime qualification;
- editor UI;
- final game runtime;
- ADF/CD32 image generation.

Those begin in later milestones after the target boundary is stable.
