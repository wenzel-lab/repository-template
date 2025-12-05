# Wenzel-Lab Hardware README Templates

This directory contains standardized README templates for Wenzel-Lab open-source hardware projects.

---

## 📁 Files in This Directory

### 1. **[HARDWARE_README_TEMPLATE.md](HARDWARE_README_TEMPLATE.md)** ⭐ Recommended
**Full-featured template for complete hardware projects**

**Use this when:**
- ✅ Your project has multiple components
- ✅ You need detailed assembly instructions
- ✅ You have associated software/firmware
- ✅ You want comprehensive documentation
- ✅ You're using GitBuilding (optional)

**Includes:**
- Complete project overview
- Detailed repository structure
- Comprehensive BOM section
- Step-by-step assembly guide
- Software/firmware documentation
- Contributing guidelines
- GitBuilding integration (optional)

### 2. **[HARDWARE_README_TEMPLATE_MINIMAL.md](HARDWARE_README_TEMPLATE_MINIMAL.md)**
**Simplified template for simple projects**

**Use this when:**
- ✅ Your project is straightforward
- ✅ You have few components
- ✅ Assembly is simple
- ✅ You want a quick start

**Includes:**
- Basic overview
- Simple BOM table
- Quick assembly steps
- Essential sections only

### 3. **[HARDWARE_README_GUIDE.md](HARDWARE_README_GUIDE.md)**
**Guide on how to use the templates**

**Use this to:**
- 📖 Learn how to customize templates
- 📖 Understand best practices
- 📖 See examples from Wenzel-Lab projects
- 📖 Avoid common mistakes

---

## 🚀 Quick Start

### For New Projects

1. **Choose a template:**
   - Complex project? → Use [HARDWARE_README_TEMPLATE.md](HARDWARE_README_TEMPLATE.md)
   - Simple project? → Use [HARDWARE_README_TEMPLATE_MINIMAL.md](HARDWARE_README_TEMPLATE_MINIMAL.md)

2. **Copy the template:**
   ```bash
   cp HARDWARE_README_TEMPLATE.md your-project/README.md
   ```

3. **Customize:**
   - Replace all `[Placeholder]` text
   - Fill in project-specific information
   - Remove sections you don't need
   - Add project-specific sections

4. **Review:**
   - Read [HARDWARE_README_GUIDE.md](HARDWARE_README_GUIDE.md) for best practices
   - Check examples from existing Wenzel-Lab projects
   - Test all links

### For Existing Projects

1. **Review your current README**
2. **Compare with templates** to identify missing sections
3. **Gradually improve** by adding missing sections
4. **Follow the guide** for best practices

---

## 📋 Template Comparison

| Feature | Full Template | Minimal Template |
|---------|--------------|------------------|
| **Overview** | ✅ Detailed | ✅ Basic |
| **Features** | ✅ Comprehensive | ✅ Key only |
| **Repository Structure** | ✅ Detailed tree | ✅ Simple list |
| **BOM** | ✅ Full with CSV/MD | ✅ Simple table |
| **Assembly Instructions** | ✅ Step-by-step with images | ✅ Brief steps |
| **Software/Firmware** | ✅ Detailed docs | ✅ Basic info |
| **Contributing Guide** | ✅ Comprehensive | ✅ Brief |
| **GitBuilding Support** | ✅ Optional section | ❌ Not included |
| **Citation** | ✅ Included | ❌ Not included |
| **Roadmap** | ✅ Included | ❌ Not included |

---

## 🎯 Which Template Should I Use?

### Use Full Template If:
- Your project has >10 components
- Assembly requires >5 steps
- You have software/firmware
- You want comprehensive documentation
- This is a research project (needs citation)
- You're using GitBuilding

### Use Minimal Template If:
- Your project has <10 components
- Assembly is straightforward (<5 steps)
- No software/firmware
- You want quick documentation
- This is a simple mechanical part

### Still Not Sure?

**Start with the Full Template** - you can always remove sections you don't need, but it's harder to add sections later.

---

## 📚 Examples from Wenzel-Lab

### Well-Documented Projects

These projects serve as good examples:

1. **[droplet-sorter-master](https://github.com/wenzel-lab/droplet-sorter-master)**
   - Master repository pattern
   - Links to sub-repositories
   - Clear overview

2. **[SiMoRa-microscope](https://github.com/wenzel-lab/SiMoRa-microscope)**
   - Detailed BOM
   - Clear assembly instructions
   - Links to original resources

3. **[syringe-pumps-and-controller](https://github.com/wenzel-lab/syringe-pumps-and-controller)**
   - Good structure
   - Clear separation of hardware/software

### Projects to Reference

- **[modular-microfluidics-workstation-controller](https://github.com/wenzel-lab/modular-microfluidics-workstation-controller)**
- **[flow-microscopy-platform](https://github.com/wenzel-lab/flow-microscopy-platform)**
- **[strobe-enhanced-microscopy-stage](https://github.com/wenzel-lab/strobe-enhanced-microscopy-stage)**

---

## 🔧 Customization Tips

### Essential Customizations

1. **Replace all placeholders:**
   - `[Project Name]` → Your project name
   - `[project-name]` → Repository name
   - `[LICENSE]` → License name
   - `[Description]` → Project description

2. **Remove unused sections:**
   - No GitBuilding? Remove GitBuilding section
   - No software? Remove Software section
   - No results? Remove Results section

3. **Add project-specific sections:**
   - Calibration procedures
   - Performance benchmarks
   - Validation results
   - Comparison with alternatives

### Optional Enhancements

- Add badges (status, license, etc.)
- Include hero image or diagram
- Add video tutorials
- Link to interactive demos
- Include 3D viewer for CAD files

---

## ✅ Checklist

Before publishing your README:

- [ ] All placeholders replaced
- [ ] BOM is accurate
- [ ] Assembly instructions are clear
- [ ] All links work
- [ ] Images are clear and properly sized
- [ ] License file included
- [ ] Repository structure matches README
- [ ] Contact information is current
- [ ] README is readable on GitHub (preview it)

---

## 🤝 Contributing to Templates

Found an issue or have a suggestion for these templates?

1. **Open an issue** describing the problem or suggestion
2. **Submit a pull request** with improvements
3. **Share examples** from your projects

---

## 📖 Additional Resources

### Documentation Standards

- [Open Hardware Documentation Template](https://github.com/SanliFaez/Open-Hardware-Documentation-Template)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
- [GitBuilding Documentation](https://gitbuilding.io/)

### Wenzel-Lab Resources

- [Wenzel-Lab GitHub](https://github.com/wenzel-lab)
- [Wenzel-Lab Website](https://wenzel-lab.github.io)
- [LIBREhub](https://github.com/LIBREhub)

---

## 📝 Template Version History

- **v1.0** (2025-01-XX): Initial release
  - Full template
  - Minimal template
  - Usage guide

---

## 💡 Tips for Success

1. **Start early**: Write README as you develop the project
2. **Be specific**: Use exact part numbers, dimensions, etc.
3. **Include images**: Show, don't just tell
4. **Test instructions**: Have someone new follow them
5. **Keep updated**: Update README when you make changes
6. **Link everything**: Make it easy to find related resources

---

## 🆘 Getting Help

### Questions?

- Check [HARDWARE_README_GUIDE.md](HARDWARE_README_GUIDE.md) for detailed guidance
- Look at examples from existing Wenzel-Lab projects
- Open an issue in this repository
- Contact Wenzel-Lab maintainers

---

**Last Updated**: 2025-01-XX  
**Maintained by**: Wenzel-Lab  
**Part of**: Wenzel-Lab Documentation Standards

---

*These templates are designed to make it easy to create comprehensive, professional documentation for open-source hardware projects. Choose the template that fits your project, customize it, and you're ready to go!*

