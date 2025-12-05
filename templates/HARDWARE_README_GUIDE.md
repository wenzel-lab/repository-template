# Wenzel-Lab Hardware README Template Guide

## Overview

This guide explains how to use the [Hardware README Template](HARDWARE_README_TEMPLATE.md) for Wenzel-Lab open-source hardware projects.

---

## When to Use This Template

Use this template for:
- ✅ Open-source hardware projects
- ✅ 3D printable devices
- ✅ Electronic projects with PCBs
- ✅ Mechanical assemblies
- ✅ Projects with associated software/firmware
- ✅ Research instrumentation

**Don't use this template for:**
- ❌ Pure software projects (use software README template instead)
- ❌ Data analysis repositories
- ❌ Documentation-only repositories

---

## Template Sections Explained

### Required Sections

These sections should be included in every hardware project README:

1. **Overview** - What is the project and why does it exist?
2. **Repository Structure** - How is the codebase organized?
3. **BOM** - What parts are needed to build it?
4. **Getting Started** - How do I begin?
5. **Assembly Instructions** - How do I build it?
6. **License** - What are the usage terms?

### Optional Sections

Include these based on your project:

- **GitBuilding Documentation** - Only if you're using GitBuilding
- **Software & Firmware** - Only if your project includes code
- **Results** - Only if you're sharing experimental data
- **Citation** - Only if this is a research project

---

## Customization Guide

### Step 1: Replace Placeholders

Search and replace throughout the template:
- `[Project Name]` → Your actual project name
- `[project-name]` → Your repository name (lowercase, hyphens)
- `[LICENSE]` → Your license name
- `[Description]` → Your project description
- `[Author Names]` → Contributor names
- `[Year]` → Current year

### Step 2: Fill in Project-Specific Content

#### Overview Section
- Write 2-3 paragraphs describing your project
- Explain the problem it solves
- Describe target users
- List key applications

#### Features Section
- List 5-10 key features
- Separate hardware vs. software features
- Highlight unique innovations

#### BOM Section
- Create `Build/BOM/BOM.csv` with all components
- Include: part name, specification, quantity, supplier, cost
- Provide both CSV (for ordering) and Markdown (for readability)

#### Repository Structure
- Customize the directory tree to match your actual structure
- Remove sections you don't use (e.g., remove `Results/` if not applicable)
- Add project-specific directories

### Step 3: Add Project-Specific Sections

Add sections unique to your project, for example:
- **Calibration Procedures**
- **Performance Specifications**
- **Validation Results**
- **Comparison with Commercial Alternatives**

---

## Directory Structure Best Practices

### Standard Structure (Recommended)

```
project-name/
├── README.md
├── LICENSE
├── Build/
│   ├── CAD/
│   ├── PCB/
│   ├── Mechanical/
│   └── BOM/
├── Docs/
│   ├── Assembly/
│   └── [other docs]
├── Software/
│   ├── firmware/
│   └── control/
└── Tests/
```

### Minimal Structure (For Simple Projects)

```
project-name/
├── README.md
├── LICENSE
├── CAD/              # Combined design files
├── BOM.csv           # Single BOM file
└── assembly.md       # Simple assembly guide
```

### Advanced Structure (For Complex Projects)

```
project-name/
├── README.md
├── LICENSE
├── Build/
│   ├── CAD/
│   ├── PCB/
│   ├── Mechanical/
│   └── BOM/
├── Docs/
│   ├── Assembly/
│   ├── User_Manual.md
│   ├── Technical_Specs.md
│   └── References/
├── Software/
│   ├── firmware/
│   ├── control/
│   └── config/
├── Tests/
│   ├── hardware_tests/
│   ├── software_tests/
│   └── results/
├── Results/          # Experimental data
│   ├── data/
│   ├── analysis/
│   └── figures/
└── .gitbuilding/     # GitBuilding docs
```

---

## GitBuilding Integration

### When to Use GitBuilding

Use GitBuilding if:
- ✅ Your project has complex assembly steps
- ✅ You want interactive documentation
- ✅ You have many components to document
- ✅ You want searchable component database

**Skip GitBuilding if:**
- ❌ Simple project with few parts
- ❌ You prefer static Markdown documentation
- ❌ You don't have time to set up GitBuilding

### GitBuilding Section in README

If using GitBuilding, include this section:

```markdown
### GitBuilding Documentation

This project uses [GitBuilding](https://gitbuilding.io/) for interactive documentation.

**View Online**: [Link to your GitBuilding site]

**Build Locally**:
```bash
pip install gitbuilding
cd .gitbuilding
gitbuilding build
gitbuilding serve
```
```

If **not** using GitBuilding, remove this section entirely.

---

## BOM Best Practices

### BOM File Formats

**Primary Format: CSV** (for ordering)
```csv
Category,Component,Specification,Quantity,Supplier,Part Number,Estimated Cost,Notes
Electronics,Microcontroller,Teensy 4.1,1,SparkFun,DEV-16796,$19.95,
Mechanical,Linear Bearing,LM8UU,4,McMaster-Carr,6384K14,$2.50,
```

**Secondary Format: Markdown** (for readability on GitHub)
```markdown
| Component | Specification | Quantity | Supplier | Cost |
|-----------|--------------|----------|----------|------|
| Microcontroller | Teensy 4.1 | 1 | SparkFun | $19.95 |
```

### BOM Organization

Organize BOM by categories:
- Electronics (PCBs, components)
- Mechanical (3D printed, machined, purchased)
- Fasteners (screws, nuts, washers)
- Other (cables, enclosures, etc.)

### Include in BOM

- ✅ Part name and specification
- ✅ Quantity needed
- ✅ Supplier and part number (if available)
- ✅ Estimated cost
- ✅ Alternative parts (if applicable)
- ✅ Notes (compatibility, substitutions)

---

## Assembly Instructions

### Structure

1. **Overview**
   - Estimated time
   - Difficulty level
   - Tools required

2. **Step-by-Step Instructions**
   - Numbered steps
   - Clear descriptions
   - Images/diagrams for each step
   - Warnings where needed

3. **Safety Precautions**
   - Electrical safety
   - Mechanical safety
   - Material handling

4. **Troubleshooting**
   - Common issues
   - Solutions

### Image Guidelines

- Use high-resolution images (minimum 1200px width)
- Show clear detail of assembly steps
- Include annotations/arrows where helpful
- Store images in `Docs/Assembly/images/`
- Use descriptive filenames: `step-01-prepare-parts.jpg`

---

## Software Documentation

### If Project Includes Software

Include:
- Installation instructions
- Configuration guide
- Usage examples
- API documentation (if applicable)

### If Project Includes Firmware

Include:
- Microcontroller model
- IDE/toolchain requirements
- Library dependencies
- Upload instructions
- Configuration settings

### Separate Software Repository?

If software is complex, consider a separate repository:
- Link to software repo in main README
- Keep basic usage instructions in hardware README

---

## Examples from Wenzel-Lab

### Well-Optimized Examples

1. **[droplet-sorter-master](https://github.com/wenzel-lab/droplet-sorter-master)**
   - Good: Clear overview, structured documentation
   - Good: Links to related repositories
   - Note: Master repository pattern for multi-repo projects

2. **[SiMoRa-microscope](https://github.com/wenzel-lab/SiMoRa-microscope)**
   - Good: Detailed BOM with part numbers
   - Good: Clear assembly instructions
   - Good: Links to original SQUID resources

3. **[syringe-pumps-and-controller](https://github.com/wenzel-lab/syringe-pumps-and-controller)**
   - Good: Separate sections for hardware and software
   - Good: Clear file structure

### Patterns to Adopt

- **Multi-repo projects**: Use a "master" repository that links to sub-repositories
- **Forked projects**: Clearly credit original project and document modifications
- **Research projects**: Include citation information
- **Modular projects**: Document how modules work together

---

## Checklist for New Projects

### Before Publishing

- [ ] README.md is complete and follows template
- [ ] All placeholder text is replaced
- [ ] BOM is accurate and includes suppliers
- [ ] Assembly instructions are clear with images
- [ ] Software/firmware is documented
- [ ] License file is included
- [ ] Repository structure matches README description
- [ ] Links are working
- [ ] Images are properly sized and clear
- [ ] Contact information is current

### Quality Checks

- [ ] README is readable on GitHub (preview it)
- [ ] All file paths in README are correct
- [ ] BOM can be opened in spreadsheet software
- [ ] Assembly instructions are testable by someone new
- [ ] Software installation works on clean system
- [ ] License is appropriate for open hardware

---

## Common Mistakes to Avoid

### ❌ Don't Do This

1. **Leaving placeholder text**
   - Bad: `[Project Name]`
   - Good: `Droplet Sorter v2.0`

2. **Broken links**
   - Bad: `[link-to-docs](docs/)` (relative path doesn't exist)
   - Good: `[link-to-docs](Docs/User_Manual.md)`

3. **Missing critical information**
   - Bad: BOM without quantities
   - Good: Complete BOM with all details

4. **Unclear assembly steps**
   - Bad: "Assemble the parts"
   - Good: "Step 1: Insert M3x6mm screw through hole A into part B..."

5. **Outdated information**
   - Bad: "Last updated: 2020"
   - Good: Keep dates current

### ✅ Do This Instead

1. **Be specific**
   - Use exact part numbers
   - Include dimensions
   - Specify materials

2. **Include images**
   - Show, don't just tell
   - Use annotations
   - Multiple angles if needed

3. **Test your instructions**
   - Have someone new follow them
   - Fix unclear steps
   - Add missing information

4. **Keep it updated**
   - Update when you make changes
   - Remove outdated information
   - Add new features to README

---

## Template Variations

### Minimal Template (For Simple Projects)

If your project is very simple, you can use a minimal version:

```markdown
# [Project Name]

Brief description.

## BOM
[Simple table]

## Assembly
[Brief steps]

## License
[License name]
```

### Advanced Template (For Complex Projects)

For complex projects, you may need additional sections:
- Performance Benchmarks
- Validation Results
- Comparison with Alternatives
- Future Improvements
- Known Limitations

---

## Integration with Other Documentation

### GitBuilding

If using GitBuilding:
- Keep README.md as entry point
- Link to GitBuilding for detailed docs
- GitBuilding handles interactive assembly guides

### Separate Documentation Site

If you have a documentation website:
- Link from README
- Keep README as GitHub landing page
- Ensure README has essential info (don't require external site)

### Wiki

If using GitHub Wiki:
- Link from README
- Use README for overview
- Use Wiki for detailed guides

---

## Maintenance

### Keep README Updated

- Update when you:
  - Add new features
  - Change BOM
  - Improve assembly process
  - Update software
  - Fix issues

### Version Your README

Consider adding version info:
```markdown
**README Version**: 1.2  
**Last Updated**: 2025-01-XX  
**Project Version**: v2.0
```

---

## Getting Help

### Questions About This Template?

- Open an issue in this repository
- Contact Wenzel-Lab maintainers
- Check existing Wenzel-Lab projects for examples

### Improving This Template

Contributions welcome! If you have suggestions:
1. Open an issue with your suggestion
2. Or submit a pull request with improvements

---

## Quick Reference

### Essential Sections (Minimum)

```markdown
# Project Name
[Description]

## BOM
[Table]

## Assembly
[Steps]

## License
[License]
```

### Recommended Sections

```markdown
# Project Name
## Overview
## Features
## Repository Structure
## BOM
## Getting Started
## Assembly Instructions
## Software/Firmware
## Usage
## Contributing
## License
## Acknowledgments
```

### Full Template

See [HARDWARE_README_TEMPLATE.md](HARDWARE_README_TEMPLATE.md) for complete template with all sections.

---

**Last Updated**: 2025-01-XX  
**Template Version**: 1.0  
**Maintained by**: Wenzel-Lab

