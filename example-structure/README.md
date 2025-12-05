# Example Instrument Structure

This directory contains an example file structure following the Wenzel-Lab instrument software design guide.

## Purpose

This is a **reference implementation** showing:
- How to organize files according to the guide
- Example implementations of ABCs, controllers, and GUI
- Configuration file structure
- Test organization

## Structure

```
example-structure/
├── instrument-config.yaml    # Main configuration file
├── requirements.txt          # Simple dependency list (no pyproject.toml needed!)
├── instrument/               # Main package (no src/ folder - simpler!)
│   ├── __init__.py
│   ├── config.py            # Configuration loading
│   ├── devices/             # Device abstractions
│   ├── controllers/         # Experiment logic
│   ├── gui/                 # GUI components
│   └── main.py              # Entry point (run with: python -m instrument.main)
└── tests/                   # Test files
```

## Key Features

- ✅ **Simple structure** - No `src/` folder, no `pyproject.toml`
- ✅ **Uses `requirements.txt`** - Easy to understand
- ✅ **Complete examples** - Shows ABCs, controllers, GUI patterns
- ✅ **Simulated devices** - Can run without hardware

## Usage

This is **not a runnable project** - it's a template showing the structure. To use it:

1. Copy this structure to your new project
2. Implement actual device drivers in `devices/`
3. Add your controllers in `controllers/`
4. Build your GUI in `gui/`
5. Customize `instrument-config.yaml` for your hardware

## Key Files

- **instrument-config.yaml**: Single source of truth for configuration
- **requirements.txt**: Simple list of dependencies (easier than pyproject.toml)
- **devices/base.py**: Abstract base classes for all devices
- **devices/simulated_.py**: Example simulated device implementations
- **controllers/**: Example controllers showing the pattern
- **gui/**: Example GUI structure (one widget per file)

## See Also

- [INSTRUMENT_SOFTWARE_GUIDE.md](../templates/guides/INSTRUMENT_SOFTWARE_GUIDE.md) - Complete guide
- [QUICK_START.md](../templates/guides/QUICK_START.md) - Beginner-friendly explanation
- [README.md](../README.md) - Repository template overview

