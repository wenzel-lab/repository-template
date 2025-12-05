# Wenzel-Lab Naming Conventions & Acronym Guidelines

This document defines naming conventions for folders, files, repositories, and instruments across Wenzel-Lab projects.

---

## 📛 General Naming Structure

### File and Folder Names

- **Use lowercase with hyphens (kebab-case)** for all file and folder names
  - `raw-data`, `control-software`, `user-guide.md` (good)
  - `RawData`, `control_software`, `user guide.md` (bad)

### Repository Names

Repository names should be:
- **Short and descriptive**
- **In kebab-case**
- **Include the acronym** (if applicable) and a descriptive function or context
  - `ritmo-sorter`, `clave-lightsheet`, `rio-controller` (good)
  - `RITMO_Sorter`, `clave lightsheet`, `rio_controller` (bad)

### What to Avoid

- Capital letters (except in acronyms when appropriate) - avoid
- Underscores - avoid
- Spaces - avoid
- Cryptic abbreviations - avoid

### Version Labels

Version folders or files may use:
- `v1.0`, `v1.1-dev`, `v2.0-beta`

---

## 🎵 Instrument Acronyms (RITMO, CLAVE, etc.)

We intentionally use **playful, culturally resonant acronyms** to name our modular instruments. The goal is to:

- **Foster recognition and engagement** through familiar or fun names
- **Celebrate Latin American identity**, particularly through references to:
  - **Music** (e.g. RITMO, CLAVE, BACHATA, TANGO, SONIDO)
  - **Spanish or Portuguese words** that are meaningful or metaphorical
    - e.g., RIO ("river") for fluid control
- **Avoid sterile or overly technical names** when the tool is meant to be adaptable, modular, or community-driven

### ✍️ Acronym Style Guidelines

- Acronyms should form a **recognizable or pronounceable word**
- The acronym letters do **not need to match the first letter of every word** — they can be embedded creatively, as long as:
  - The expanded phrase is technically accurate
  - The meaning of each letter is explained in the README
- **Avoid forced or awkward expansions** — clarity and creativity are both valued

### Examples

| Acronym | Stands for | Description |
|---------|------------|-------------|
| **RITMO** | Real-time Instrument for Microfluidic Droplet Sorting and Optical analysis | A droplet sorter with flow-cytometry-like functionality |
| **CLAVE** | Cubes and Light-sheet Apparatus for Versatile Experiments | A modular UC2-based light-sheet microscope |
| **RIO** | (Name only, from "river" in Spanish) | Fluid control unit using pressure and feedback |
| **BACHATA** | Bio-Atmospheric Chamber for Cell and Anaerobic Testing and Analysis | A controlled-atmosphere incubator |
| **SONIDO** | System for Optical Non-Invasive Diagnostic Operations | Spectroscopy and optical diagnostics platform |

---

## 🔖 Labeling Instruments and Modules

- **Instrument acronyms** (e.g., RITMO) should be used consistently across repos, diagrams, and documentation
- **Submodules** (e.g., "control box", "sorter head", "illumination") should also follow kebab-case:
  - `ritmo-sorter-head`, `clave-illumination-module` (good)
  - `ritmo_sorter_head`, `CLAVE_Illumination` (bad)
- Consider adding **nickname tags** in metadata or internal README sections if the acronym is meant to resonate beyond just a technical label

---

## Quick Reference

### File Naming
```
Good:              Bad:
user-guide.md         UserGuide.md
control-software/     control_software/
assembly-v2/          assembly v2/
```

### Repository Naming
```
Good:              Bad:
ritmo-sorter          RITMO_Sorter
clave-lightsheet      clave lightsheet
rio-controller        RIOController
```

### Module Naming
```
Good:              Bad:
ritmo-sorter-head     ritmo_sorter_head
clave-illumination    CLAVE_Illumination
rio-pump-module       RIO_Pump_Module
```

---

**Last Updated**: 2025-01-XX  
**Maintained by**: Wenzel-Lab

