# Wenzel-Lab Repository Template [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

The Wenzel-Lab template for building **Python-based laboratory instrument software** and **open hardware documentation** repositories.

This repository serves as:
- **Template** - Copy this structure when starting new projects
- **Reference** - Find guides and conventions used in Wenzel-Lab
- **Standard** - Ensure consistency across all Wenzel-Lab repositories

For more resources on open-source hardware for bioimaging, see [LIBRE Hub](https://github.com/LIBREhub) and the [Wenzel Lab website](https://wenzel-lab.github.io/en/).

---

## Quick Start

### For New Projects

1. **Use this as a template:**
   ```bash
   # On GitHub: Click "Use this template" button
   # Or locally:
   git clone https://github.com/wenzel-lab/repository-template.git your-project-name
   cd your-project-name
   rm -rf .git
   git init
   ```

2. **Follow the guides:**
   - **New to software?** Start with [templates/guides/QUICK_START.md](templates/guides/QUICK_START.md) - explains basics in simple terms
   - **Software projects**: [Guide to software design for instrument control](templates/guides/instrument-software-guide.md)
   - **Hardware projects**: See [templates/hardware-readme-guide.md](templates/hardware-readme-guide.md)

3. **Customize:**
   - Replace placeholder text
   - Add project-specific files
   - Remove unused sections

---

## Contents

### Software Development

#### [Guide to software design for instrument control](templates/guides/instrument-software-guide.md)

Complete guide for building Python-based instrument control software:

- **Repository structure** - Standard folder layout (with simple alternatives explained)
- **Configuration** - Single YAML config file pattern
- **Device abstraction** - ABC-based hardware abstraction layer
- **PyVISA integration** - For SCPI/VISA instruments
- **Controllers** - Experiment and live view logic
- **GUI** - Qt-based interface guidelines
- **Simulation** - Testing without hardware
- **AI assistant instructions** - How AI should follow these conventions

**Key principles:**
- Single config file at root (`instrument-config.yaml`)
- ABC-based device abstraction (no global state)
- Controllers and models separate from GUI (viewer)
- Simulation mode for all devices
- Simple, maintainable architecture

#### [templates/guides/QUICK_START.md](templates/guides/QUICK_START.md) **New to Software? Start Here!**

Beginner-friendly guide explaining:
- When to use simple vs. advanced structure
- Step-by-step getting started

### Naming and Conventions

#### [templates/guides/NAMING_CONVENTIONS.md](templates/guides/NAMING_CONVENTIONS.md)

Guidelines for naming files, folders, repositories, and instruments:

- **File naming** - Use kebab-case (lowercase with hyphens)
- **Repository naming** - Short, descriptive, include acronyms
- **Instrument acronyms** - Latin American, playful, culturally resonant names (RITMO, CLAVE, RIO, etc.)
- **Module labeling** - Consistent naming across projects

### Licensing

#### [templates/guides/LICENSING_GUIDE.md](templates/guides/LICENSING_GUIDE.md)

Guide for choosing and applying licenses:

- **Hardware designs** - CERN Open Hardware Licence 2.0 (Weakly Reciprocal)
- **Software code** - GNU General Public License 3.0 (GPL-3.0)
- **Alternative for documents** - Creative Commons Attribution 4.0 (CC-BY-4.0)

License files are available in `templates/` for easy copying.

### Hardware Documentation

#### [templates/](templates/) - README Templates for Hardware Projects

Templates and guides for documenting open-source hardware projects:

- **[HARDWARE_README_TEMPLATE.md](templates/HARDWARE_README_TEMPLATE.md)** - Full-featured template
- **[HARDWARE_README_TEMPLATE_MINIMAL.md](templates/HARDWARE_README_TEMPLATE_MINIMAL.md)** - Simplified template
- **[hardware-readme-guide.md](templates/hardware-readme-guide.md)** - How to use the templates

**Use these for:**
- 3D printable devices
- Optomechanic projects (microscopes etc.)
- Electronic projects with PCBs
- Mechanical assemblies
- Projects with associated software/firmware

---

### Example Repository Structure

See **[example-structure/](example-structure/)** for a complete reference implementation.

The example shows the **simplified structure** (no `src/` folder, uses `requirements.txt`):

```
instrument-name/
├── README.md
├── instrument-config.yaml         # Main config file
├── requirements.txt               # Simple dependency list
├── instrument/                    # Main Python package (no src/ folder!)
│   ├── __init__.py
│   ├── config.py
│   ├── devices/                   # Device abstractions
│   ├── controllers/               # Experiment logic
│   ├── gui/                       # GUI components
│   └── main.py                    # Entry point (like SQUID)
└── tests/                         # Test files
```

**See [Guide to software design for instrument control](templates/guides/instrument-software-guide.md) for detailed explanations.**

---

## 🎯 Design Principles

### Software Architecture

1. **Layered Architecture**
   - Drivers → ABCs → Controllers → GUI
   - Clear separation of concerns

2. **Configuration-Driven**
   - Single `instrument-config.yaml` at root
   - No global configuration state
   - Pydantic models for validation

3. **Device Abstraction**
   - Abstract Base Classes (ABCs) for all devices
   - PyVISA for SCPI instruments
   - Simulation mode for all devices

4. **Simplicity First**
   - Start simple, add complexity only when needed
   - Avoid over-engineering
   - Clear, readable code

### Documentation Standards

1. **Comprehensive READMEs**
   - Clear overview and features
   - Complete BOM for hardware
   - Step-by-step assembly instructions
   - Usage examples

2. **Structured Documentation**
   - Consistent folder structure
   - Clear file naming
   - Links between related docs

3. **Open Hardware**
   - All design files available
   - Clear licensing
   - Reproducible builds

---

## 📖 Guides and References

### For Software Development

- **[templates/guides/QUICK_START.md](templates/guides/QUICK_START.md)** - Start here if you're new to software! Explains basics in simple terms
- **[Guide to software design for instrument control](templates/guides/instrument-software-guide.md)** - Complete software architecture guide
- **[templates/guides/NAMING_CONVENTIONS.md](templates/guides/NAMING_CONVENTIONS.md)** - Naming guidelines for files, repos, and instruments
- **[templates/guides/LICENSING_GUIDE.md](templates/guides/LICENSING_GUIDE.md)** - License selection and usage
- **Python for the Lab** - Foundational concepts
- **Experimentor** - MVC-style framework examples
- **SQUID** (Cephla-Lab/Squid) - Microscope control patterns
- **ImSwitch** - Plugin-based microscope control

### For Hardware Documentation

- **[templates/HARDWARE_README_TEMPLATE.md](templates/HARDWARE_README_TEMPLATE.md)** - Full hardware README template
- **[templates/HARDWARE_README_TEMPLATE_MINIMAL.md](templates/HARDWARE_README_TEMPLATE_MINIMAL.md)** - Minimal template
- **[templates/hardware-readme-guide.md](templates/hardware-readme-guide.md)** - Template usage guide

### License Information

See [templates/guides/LICENSING_GUIDE.md](templates/guides/LICENSING_GUIDE.md) for:
- Which license to use for hardware, software, and documentation
- Links to download official license texts
- How to add licenses to your project

### Example Projects

See existing Wenzel-Lab repositories for examples:
- [droplet-sorter-master](https://github.com/wenzel-lab/droplet-sorter-master)
- [SiMoRa-microscope](https://github.com/wenzel-lab/SiMoRa-microscope)
- [flow-microscopy-platform](https://github.com/wenzel-lab/flow-microscopy-platform)
- [modular-microfluidics-workstation-controller](https://github.com/wenzel-lab/modular-microfluidics-workstation-controller)

---

## ✅ Checklist for New Projects

### Software Projects

- [ ] Repository structure matches [Guide to software design for instrument control](templates/guides/instrument-software-guide.md)
- [ ] Single `instrument-config.yaml` at root
- [ ] Device ABCs defined in `devices/base.py`
- [ ] PyVISA used for SCPI devices (wrapped in ABCs)
- [ ] Controllers take devices via constructor (no globals)
- [ ] GUI code separate from business logic
- [ ] Simulation mode available for all devices
- [ ] Tests present (even if minimal)

### Hardware Projects

- [ ] README follows template from [templates/](templates/)
- [ ] Complete BOM with suppliers and part numbers
- [ ] Clear assembly instructions with images
- [ ] All design files in `Build/` directory
- [ ] Software/firmware documented (if applicable)
- [ ] License file included

---

## 🤝 Contributing

Found an issue or have a suggestion for this template?

1. **Open an issue** describing the problem or suggestion
2. **Submit a pull request** with improvements
3. **Share examples** from your projects

Contacts and more:
- **Wenzel-Lab GitHub**: [https://github.com/wenzel-lab](https://github.com/wenzel-lab)
- **Wenzel-Lab Website**: [https://wenzel-lab.github.io](https://wenzel-lab.github.io)
- **LIBREhub**: [https://github.com/LIBREhub](https://github.com/LIBREhub)

---

## License

**This project is Open Source** - please acknowledge us when using this template or sharing modifications externally.



