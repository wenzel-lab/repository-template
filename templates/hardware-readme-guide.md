# Wenzel-Lab Hardware README Guide

This guide explains how to use the hardware README templates for Wenzel-Lab open-source hardware projects.

---

## Templates Available

### [HARDWARE_README_TEMPLATE.md](HARDWARE_README_TEMPLATE.md)
Full-featured template for complete hardware projects.

**Use this when:**
- Your project has multiple components
- You need detailed assembly instructions
- You have associated software/firmware
- You want comprehensive documentation

### [HARDWARE_README_TEMPLATE_MINIMAL.md](HARDWARE_README_TEMPLATE_MINIMAL.md)
Simplified template for straightforward projects.

**Use this when:**
- Your project is straightforward
- You have few components
- Assembly is simple
- You want a quick start

---

## GitBuilding vs. Non-GitBuilding Projects

### Using GitBuilding (Extensive Documentation)

**When to use:**
- Your project requires extensive documentation for community replication
- You want interactive, structured documentation with searchable components
- You have many components to document

**What to include:**
- **Do NOT include BOM section** - GitBuilding generates this automatically
- Include GitBuilding documentation section
- All other standard sections

### Not Using GitBuilding

**When to skip:**
- Projects that require high expertise to build (simpler documentation needs, but always include complete source files)
- Early stages of development
- You prefer static Markdown documentation

**What to include:**
- **Include one or more BOM tables** with components, specifications, quantities, and costs
- Standard Markdown documentation
- All source files must be shared (CAD, PCB, etc.)

---

## Quick Start

1. **Choose a template** based on your project needs
2. **Copy the template** to your project as `README.md`
3. **Customize:**
   - Replace all `[Placeholder]` text
   - Fill in project-specific information
   - Remove sections you don't need (e.g., remove BOM if using GitBuilding)
4. **Review** against examples from existing Wenzel-Lab projects

---

## Key Sections

### Required Sections
- **Overview** - What is the project and why does it exist?
- **Repository Structure** - How is the codebase organized?
- **BOM** - Component tables (only if NOT using GitBuilding)
- **Getting Started** - How do I begin?
- **Assembly Instructions** - How do I build it?
- **Contribute** - How to contribute (includes contact info)
- **License** - Usage terms

### Optional Sections
- **GitBuilding Documentation** - Only if using GitBuilding
- **Software & Firmware** - Only if your project includes code
- **Citation** - Only if this is a research project

---

## Customization

### Essential Steps

1. **Replace placeholders:**
   - `[Project Name]` → Your project name
   - `[project-name]` → Repository name (lowercase, hyphens)
   - `[LICENSE]` → License name
   - `[Description]` → Project description

2. **Remove unused sections:**
   - No GitBuilding? Remove GitBuilding section and include BOM tables
   - Using GitBuilding? Remove BOM section
   - No software? Remove Software section

3. **Add project-specific content:**
   - BOM tables (if not using GitBuilding)
   - Assembly instructions
   - Calibration procedures (if applicable)

---

## Contributing Section

The contributing section should:
- Welcome contributions and questions
- Include GOSH Code of Conduct reference
- Accept questions via issues (not just code submissions)
- Include contact information (Wenzel Lab, LIBRE Hub, GitHub links)
- Be concise - no separate contribution guide document needed

---

## Examples

Good examples from Wenzel-Lab:
- [syringe-pumps-and-controller](https://github.com/wenzel-lab/syringe-pumps-and-controller) - GitBuilding documentation
- [SiMoRa-microscope](https://github.com/wenzel-lab/SiMoRa-microscope) - Detailed BOM and assembly

---

## Checklist

Before publishing:
- [ ] All placeholders replaced
- [ ] BOM included (if not using GitBuilding) or GitBuilding section included
- [ ] Assembly instructions are clear
- [ ] All links work
- [ ] Contributing section includes contact info
- [ ] License file included
- [ ] Source files are shared (CAD, PCB, etc.)

---

**Last Updated**: 2025-01-XX  
**Maintained by**: Wenzel-Lab

