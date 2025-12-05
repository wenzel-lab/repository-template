# Wenzel-Lab Instrument Software Design Guide

This document defines the standard software structure for **modern, open-source, Python-based laboratory instrumentation** in Wenzel-Lab.

It is written for:

- **Humans** (developers, students, collaborators), and  
- **AI coding assistants** (e.g. Cursor, ChatGPT) that should follow these conventions when creating or refactoring code for Wenzel-Lab instruments.

## Baseline Assumptions

- Target platform: **Linux desktop** (or laptop).
- Standard usage: launch **from the terminal**, start a **GUI** for normal operation.
- Typical stack: Python 3, Qt-based GUI (via `qtpy` + `PyQt5`/`PySide`), optional napari.
- Main focus: **simple, maintainable architectures** that can grow in complexity when needed, but do not start as full-blown frameworks.

---

## 1. Repository Skeleton (Standard Pattern)

A typical Wenzel-Lab instrument software repository should follow this minimal structure:

```text
instrument-name/
├── README.md                      # Project overview (hardware + software)
├── INSTRUMENT_SOFTWARE_GUIDE.md   # (Optional) This guide, or link to it
├── instrument-config.yaml         # Main config file (single source of truth)
├── requirements.txt               # Simple dependency list (or pyproject.toml - see explanation below)
├── instrument/                    # Main Python package (no src/ folder - simpler!)
│   ├── __init__.py
│   ├── config.py                  # Pydantic or simple loader around YAML
│   ├── devices/                   # Device abstractions and drivers
│   │   ├── base.py                # ABCs for all device types
│   │   ├── camera_.py
│   │   ├── pump_.py
│   │   ├── valve_.py
│   │   ├── sensor_.py
│   │   └── simulated_.py           # Simulation implementations
│   ├── controllers/               # Experiment / protocol logic
│   │   ├── live_controller.py
│   │   └── experiment_controller.py
│   ├── gui/                       # Qt GUI code
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   └── widgets/               # One widget per file, not monolithic
│   │       ├── camera_widget.py
│   │       ├── pump_widget.py
│   │       └── status_widget.py
│   └── main.py                    # Entry point: build devices, controllers, GUI
└── tests/
    ├── test_devices.py
    ├── test_controllers.py
    └── test_gui_smoke.py
```

### 📁 Understanding the Structure

#### Why `src/` folder?

**What it is:** `src` stands for "source" - it's a folder that contains all your Python code.

**Why use it?** This is a Python best practice that:
- **Prevents import confusion**: Without `src/`, Python might accidentally import from your working directory instead of your installed package
- **Separates code from other files**: Keeps your Python code separate from config files, README, tests, etc.
- **Makes installation cleaner**: When you install your package, only the `src/` contents get installed

**Is it required?** No! If you find it confusing, you can use a simpler structure:

```text
instrument-name/
├── instrument/          # Your Python package (no src/ folder)
│   ├── __init__.py
│   ├── devices/
│   └── ...
├── tests/
└── ...
```

**Recommendation:** Start simple! If your project is small and you're just learning, skip the `src/` folder. You can always add it later if needed.

#### What is `pyproject.toml`?

**What it is:** `pyproject.toml` is a configuration file (TOML = "Tom's Obvious Minimal Language") that tells Python tools about your project.

**What it does:**
- Lists your dependencies (what packages your code needs)
- Defines project metadata (name, version, description)
- Configures tools (like code formatters, linters)

**Do you need it?** Not strictly! You can use simpler alternatives:

**Option 1: `requirements.txt` (Simplest)**
```text
# requirements.txt
numpy>=1.20.0
pyvisa>=1.13.0
pyqt5>=5.15.0
```

**Option 2: `pyproject.toml` (More modern, recommended)**
- Better for complex projects
- Can configure multiple tools in one file
- Standard for modern Python projects

**Recommendation:** For beginners, start with `requirements.txt`. It's simpler and easier to understand. You can switch to `pyproject.toml` later if you want.

### 🎯 Simplified Structure (For Beginners)

If the `src/` folder and `pyproject.toml` seem too complex, here's a simpler version:

```text
instrument-name/
├── README.md
├── instrument-config.yaml
├── requirements.txt              # Simple dependency list
├── instrument/                   # Your Python code (no src/ folder)
│   ├── __init__.py
│   ├── devices/
│   ├── controllers/
│   ├── gui/
│   └── main.py                   # Entry point (like SQUID)
└── tests/
```

**This works just fine!** The `src/` and `pyproject.toml` are "nice to have" but not required for small projects.

**Key points:**

- Single config file at top level: `instrument-config.yaml`.
- Your Python package (with `__init__.py`) can be directly in the root or in `src/` - both work!
- `devices/` holds all device abstractions and drivers.
- `controllers/` holds high-level logic (live view, experimental protocols).
- `gui/` holds GUI code (no business logic).
- Simulation lives alongside real drivers (`simulated_.py`).
- Tests are present from the start, even if minimal.
- **Entry point is `main.py`** (like SQUID) - run with `python -m instrument.main` or `python instrument/main.py`

---

## 2. Configuration: Single Root File

Use one main config file at the repository root, e.g.:

```yaml
# instrument-config.yaml

instrument_name: "flow-microscopy-platform"

simulation: false

camera:
  type: "Daheng"
  serial_number: "GX123456"
  exposure_ms: 20.0

pumps:
  - name: "sample_pump"
    backend: "pyvisa"
    resource: "USB0::0x1AB1::0x0E11::DP8C123456789::INSTR"
    flow_unit: "uL/min"
  - name: "sheath_pump"
    backend: "serial"
    port: "/dev/ttyUSB0"
    baudrate: 115200

valves:
  - name: "sorting_valve"
    backend: "gpio"
    channel: 17

paths:
  data_root: "/data/flow-experiments"
```

**Recommended pattern:**

- Load this YAML into a configuration object (preferably via Pydantic).
- Pass that object into your top-level `main.py` (no global `_def.py` style constants).
- Keep derived or cached values inside managers/controllers, not in the raw config.

---

## 3. Device Abstraction Layer (ABCs + Concrete Drivers)

### 3.1 Goals

- Separate "what" from "how":
  - "What" the instrument needs: `set_flow_rate`, `get_frame`, `switch_channel`.
  - "How" a particular device does it: PyVISA, serial, vendor SDK, GPIO, etc.
- Allow:
  - Switching device models without changing experiment logic.
  - Simulation without hardware.

### 3.2 Minimal ABC pattern (baseline)

Create simple abstract base classes in `devices/base.py`:

```python
# instrument/devices/base.py

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, Any

class Device(ABC):
    """Base class for all devices."""
    
    @abstractmethod
    def initialize(self) -> None:
        ...
    
    @abstractmethod
    def close(self) -> None:
        ...

class Camera(Device):
    @abstractmethod
    def grab_frame(self) -> Any:  # replace Any with np.ndarray in real code
        ...

class Pump(Device):
    @abstractmethod
    def set_flow_rate(self, rate_ul_min: float) -> None:
        ...
    
    @abstractmethod
    def get_flow_rate(self) -> float:
        ...
```

Concrete drivers are then small, readable classes in `devices/camera_.py`, `devices/pump_.py`, etc.

---

## 4. PyVISA and PyVISA-sim Integration

### 4.1 What PyVISA provides

PyVISA is a Python package that wraps the VISA standard to control instruments over GPIB, RS-232, Ethernet, or USB.

**Key features:**

- A `ResourceManager` to list and open VISA resources.
- A uniform resource string format, e.g.:
  - `USB0::0x1234::0x5678::INSTR`
  - `TCPIP::192.168.1.10::INSTR`
- High-level methods like `write()`, `read()`, `query()` for SCPI-style instruments.

**PyVISA backends:**

- Vendor VISA libraries (NI, Keysight, etc.).
- **PyVISA-py** – a pure Python backend implementing VISA in Python.

### 4.2 PyVISA-sim: simulation backend

PyVISA-sim is a PyVISA backend that simulates VISA instruments, using text/YAML configuration to define virtual instruments and responses.

**Benefits:**

- You can fully test your instrument drivers and experiment logic without having the physical instrument.
- Continuous integration can run with simulated hardware.
- Great for teaching and onboarding: students can run examples at home.

### 4.3 Recommended pattern for Wenzel-Lab

For any SCPI / VISA-capable device (power supplies, syringe pumps with SCPI, function generators, some spectrometers):

1. Use PyVISA as the underlying communication layer.
2. Wrap it in your own ABC-based driver, so the rest of the code never sees PyVISA directly.

**Example driver:**

```python
# instrument/devices/pump_.py

from __future__ import annotations
from dataclasses import dataclass
import pyvisa  # type: ignore
from .base import Pump

@dataclass
class PyVisaPumpConfig:
    resource: str  # e.g. "USB0::0x1AB1::0x0E11::DP8C123456789::INSTR"

class PyVisaPump(Pump):
    def __init__(self, config: PyVisaPumpConfig) -> None:
        self._config = config
        self._rm: pyvisa.ResourceManager | None = None
        self._inst: pyvisa.resources.MessageBasedResource | None = None
        self._current_rate: float = 0.0
    
    def initialize(self) -> None:
        self._rm = pyvisa.ResourceManager()
        self._inst = self._rm.open_resource(self._config.resource)
        # Optional: configure termination, timeouts, etc.
        self._inst.write("*RST")
    
    def close(self) -> None:
        if self._inst is not None:
            self._inst.close()
        if self._rm is not None:
            self._rm.close()
    
    def set_flow_rate(self, rate_ul_min: float) -> None:
        self._current_rate = rate_ul_min
        # Example SCPI (device-specific)
        self._inst.write(f"FLOW {rate_ul_min}UL/MIN")
    
    def get_flow_rate(self) -> float:
        # Some pumps may not support queries; in that case, return cached value
        return self._current_rate
```

**For simulation:**

- Use PyVISA-sim as the backend (configured via environment or VISA library string).
- Provide a YAML describing your simulated pump.
- Or implement a simple `SimulatedPump` that subclasses `Pump` and only keeps internal state.

**For non-VISA devices** (GPIO valves, simple UART pumps, home-built electronics):

- Use the same ABCs (`Pump`, `Valve`, `Sensor`), but implement them with:
  - `pyserial`, custom binary protocol,
  - `RPi.GPIO` (or similar),
  - vendor SDKs, etc.

The experiment logic does not care whether a pump is PyVISA-based or serial-based as long as it sees the `Pump` interface.

---

## 5. Controllers: Live and Experiment Logic

Controllers consume ABC devices and implement workflows.

**Typical files:**

- `controllers/live_controller.py` – streaming camera previews, toggling illumination, simple focus controls.
- `controllers/experiment_controller.py` – acquisition loops, flow ramps, time series.

**Structure:**

- Controllers take devices (or managers) via constructor (no globals):

```python
# instrument/controllers/experiment_controller.py

from __future__ import annotations
from dataclasses import dataclass
from instrument.devices.base import Camera, Pump

@dataclass
class ExperimentParams:
    flow_rate_ul_min: float
    duration_s: float

class ExperimentController:
    def __init__(self, camera: Camera, pump: Pump) -> None:
        self._camera = camera
        self._pump = pump
    
    def run_experiment(self, params: ExperimentParams) -> None:
        self._pump.set_flow_rate(params.flow_rate_ul_min)
        # simple blocking loop for now
        # (later you can introduce threading or asyncio if needed)
        for _ in range(int(params.duration_s)):
            frame = self._camera.grab_frame()
            self._save_frame(frame)
            # sleep 1s etc.
    
    def _save_frame(self, frame) -> None:
        # Minimal placeholder; real code writes to disk / Zarr / OME-TIFF
        pass
```

Later, if needed, you can introduce:

- Threads for camera acquisition,
- Async I/O for fast microfluidics actions,
- State machines for complex protocols.

The guide does not require those advanced layers by default, but you should design controllers so that they can evolve in that direction without breaking everything.

---

## 6. GUI: Simple, Static, and Separate

For many Wenzel-Lab devices (flow platforms, incubators, simple microscopes), a small, static GUI is enough:

- A main window with:
  - A live image view (if there is a camera),
  - Tabbed controls for pumps, valves, and experiment presets,
  - Status display and logging.

**Guidelines:**

- Put GUI code under `instrument/gui/` (or `src/instrument/gui/` if using src layout).
- Keep one widget per file, e.g. `camera_widget.py`, `pump_widget.py`.
- GUI should call controllers and devices via well-defined methods; it should not implement hardware logic directly.
- Use Qt signals/slots to communicate between GUI and background workers, if/when you introduce threads.

**For more advanced imaging devices** that require:

- napari integration,
- flexible multi-modal control,
- plugin-driven configuration,

you may choose to:

- Study and reuse ideas from **SQUID** ([Cephla-Lab/Squid](https://github.com/Cephla-Lab/Squid)), which uses a manager/controller/gui structure with extensive imaging features.
- Consider using **ImSwitch** ([imswitch](https://github.com/kasasxav/imswitch)) directly as the main application and writing only hardware plugins for it.

---

## 7. Simulation Strategy

Simulation is a core requirement:

- Drivers should always have a plausible simulated version.
- Controllers and GUI should work with simulated drivers.

**Approach:**

1. **PyVISA Devices**
   - Use PyVISA-sim with a suitable configuration file to simulate SCPI instruments.
   - Run tests and examples without hardware.

2. **Non-VISA Devices**
   - Implement `SimulatedCamera`, `SimulatedPump`, etc., which:
     - Maintain internal state,
     - Return plausible dummy images or numeric values,
     - Log actions instead of touching real hardware.

3. **Configuration hook**
   - Controlled via `instrument-config.yaml` (`simulation: true/false`).
   - `main.py` chooses simulated or real drivers based on this flag.

---

## 8. Where to Look for Patterns

This guide defines the baseline architecture. For more advanced or alternative patterns, use:

- **[Python for the Lab](https://www.pythonforthelab.com/)** (book + site) – foundational concepts and examples of Python-based instrument control, including driver patterns, GUIs, and automation.
- **[Experimentor](https://github.com/aquilesC/experimentor)** – an MVC-style framework by Aquiles Carattino for experiment control; good examples of Models, Views, and Drivers for lab setups.
- **[PyVISA](https://pyvisa.readthedocs.io/) / [PyVISA-py](https://github.com/pyvisa/pyvisa-py) / [PyVISA-sim](https://github.com/pyvisa/pyvisa-sim)** – reference implementations for VISA-based communication and simulation backends.
- **[SQUID](https://github.com/Cephla-Lab/Squid)** (Cephla-Lab/Squid) – modern microscope control software with:
  - Abstract camera/stage interfaces,
  - Managers and controllers,
  - OME-TIFF/Zarr data handling,
  - Simulation modes and complex multipoint acquisition.
- **[ImSwitch](https://github.com/kasasxav/imswitch)** – MVP-based microscope control with plugin architecture and UC2 integration, useful when your instrument is primarily a microscope and you want to join a broader ecosystem.

You are encouraged to reuse patterns, not copy entire frameworks, unless the project clearly benefits from building inside ImSwitch or SQUID directly.

---

## 9. Advanced Layers (Optional, For Future Extensions)

The baseline described above is intentionally modest in complexity. For some Wenzel-Lab applications (e.g. high-speed droplet sorting, complex flow protocols, or remote control), you may later introduce:

- **State machines** for protocol execution (priming → running → washing → park).
- **Async I/O** (asyncio) for low-latency decisions (e.g. image-based sorting).
- **Remote APIs** (FastAPI, WebSockets, Hypha, etc.) for multi-client control.
- **Plugin discovery** for optional peripherals (but avoid overengineering small projects).

These are not required in the standard template, but the architecture is designed so that you can add them incrementally without a complete rewrite.

---

## 10. How AI Assistants Should Use This Guide

When an AI coding assistant is asked to:

- Refactor an existing Wenzel-Lab instrument repo, or
- Create new control software for a Wenzel-Lab device,

it should:

1. Respect the repository skeleton in Section 1 (adapted to the existing repo).
2. Implement devices via ABCs in `devices/base.py`, using PyVISA when appropriate.
3. Keep controllers and GUI separate, with controllers consuming device interfaces.
4. Support simulation either via PyVISA-sim or simulated device classes.
5. Load configuration from `instrument-config.yaml` and avoid global configuration state.
6. Use the references in Section 8 as patterns, not rigid dependencies.
7. Use `main.py` as the entry point (like SQUID), not `app.py`.

If complexity is added (state machines, async, plugin-like mechanisms), it should be justified by the instrument needs and built on top of this baseline, not instead of it.

---

## Quick Reference Checklist

When creating a new instrument repository:

- [ ] Repository follows the skeleton structure (Section 1)
- [ ] Single `instrument-config.yaml` at root (Section 2)
- [ ] Device ABCs defined in `devices/base.py` (Section 3)
- [ ] PyVISA used for SCPI devices, wrapped in ABCs (Section 4)
- [ ] Controllers take devices via constructor (Section 5)
- [ ] GUI code separate from business logic (Section 6)
- [ ] Simulation mode available for all devices (Section 7)
- [ ] Tests present (even if minimal)
- [ ] No global configuration state
- [ ] Entry point is `main.py` (not `app.py`)

---

**Last Updated**: 2025-01-XX  
**Maintained by**: Wenzel-Lab  
**Version**: 1.0
