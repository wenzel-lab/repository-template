# Wenzel-Lab Licensing Guide

This guide explains which licenses to use for different types of content in Wenzel-Lab projects.

---

## 📋 License Selection

### Hardware Designs (CAD, PCB, Mechanical Drawings)

**Use: CERN Open Hardware Licence Version 2 - Weakly Reciprocal (CERN-OHL-S-2.0)**

- **Why**: Specifically designed for open hardware
- **What it means**: Others can use, modify, and distribute your hardware designs, but if they modify and distribute, they must share their modifications
- **Download**: https://ohwr.org/cern_ohl_s_v2.txt

**When to use:**
- 3D printable parts (STL, STEP files)
- PCB designs (Gerber files, schematics)
- Mechanical drawings (DXF, PDF)
- Any hardware design files

---

### Software (Python, C++, Firmware, etc.)

**Use: GNU General Public License Version 3 (GPL-3.0)**

- **Why**: Ensures software remains free and open, compatible with open hardware philosophy
- **What it means**: Others can use, modify, and distribute your software, but any modifications must also be open source
- **Download**: https://www.gnu.org/licenses/gpl-3.0.txt

**When to use:**
- Python control software
- Firmware (Arduino, ESP32, etc.)
- C/C++ code
- Any software code

**Alternative for permissive software:**
- If you want to allow proprietary modifications, consider **MIT License** or **Apache 2.0**
- However, GPL-3.0 is recommended to maintain open-source principles

---

### Documentation (READMEs, Manuals, Guides)

**Use: Creative Commons Attribution 4.0 (CC-BY-4.0)**

- **Why**: Designed for creative works and documentation
- **What it means**: Others can use, modify, and distribute your documentation, as long as they give credit
- **Download**: https://creativecommons.org/licenses/by/4.0/legalcode

**When to use:**
- README files
- User manuals
- Assembly guides
- Technical documentation
- Images and diagrams (unless already covered by hardware license)

**Note**: If your documentation is part of a hardware project, it may already be covered by the CERN-OHL-S-2.0 license. CC-BY-4.0 is more permissive for documentation specifically.

---

## 🔄 Mixed Content Projects

Many Wenzel-Lab projects contain multiple types of content. Here's how to handle them:

### Option 1: Single License (Simplest)

If your project is primarily one type (e.g., hardware), use that license for everything:

```
LICENSE  # CERN-OHL-S-2.0 for hardware project
```

### Option 2: Multiple Licenses (More Precise)

If you have distinct hardware and software components:

```
LICENSE              # CERN-OHL-S-2.0 for hardware
LICENSE-SOFTWARE     # GPL-3.0 for software
LICENSE-DOCS         # CC-BY-4.0 for documentation
```

Then specify in your README:

```markdown
## License

- **Hardware**: CERN Open Hardware Licence Version 2 - Weakly Reciprocal
- **Software**: GNU General Public License Version 3
- **Documentation**: Creative Commons Attribution 4.0
```

---

## 📝 How to Add a License

### Step 1: Choose Your License

Based on the content type, select the appropriate license from above.

### Step 2: Add License File

Download the license text from the official source and save it as `LICENSE` in your repository:

**For hardware:**
- Download from: https://ohwr.org/cern_ohl_s_v2.txt
- Save as: `LICENSE`

**For software:**
- Download from: https://www.gnu.org/licenses/gpl-3.0.txt
- Save as: `LICENSE`

**For documentation:**
- Download from: https://creativecommons.org/licenses/by/4.0/legalcode
- Save as: `LICENSE-DOCS` (or add to main LICENSE if only docs)

**Quick copy commands:**
```bash
# Hardware (CERN-OHL-S-2.0)
curl -o LICENSE https://ohwr.org/cern_ohl_s_v2.txt

# Software (GPL-3.0)
curl -o LICENSE https://www.gnu.org/licenses/gpl-3.0.txt

# Documentation (CC-BY-4.0)
curl -o LICENSE-DOCS https://creativecommons.org/licenses/by/4.0/legalcode
```

### Step 3: Add License Notice to README

Add a license section to your README:

```markdown
## License

This project is licensed under the [License Name] - see the [LICENSE](LICENSE) file for details.
```

### Step 4: Add Copyright Notice

At the top of your LICENSE file, add:

```
Copyright (C) [Year] [Your Name/Organization]

This work is distributed under the terms of the [License Name]
(available at [license URL]).
```

---

## ❓ Common Questions

### Q: Can I use a different license?

**A**: Yes, but these are the recommended licenses for Wenzel-Lab projects to maintain consistency and open-source principles.

### Q: What if I want to allow commercial use?

**A**: 
- **Hardware**: CERN-OHL-S-2.0 allows commercial use
- **Software**: GPL-3.0 allows commercial use, but modifications must remain open source
- **Documentation**: CC-BY-4.0 allows commercial use

### Q: What if I want to allow proprietary modifications?

**A**: 
- For hardware: CERN-OHL-P (permissive) instead of CERN-OHL-S
- For software: MIT or Apache 2.0 instead of GPL-3.0
- For documentation: CC-BY-4.0 already allows this

### Q: Do I need to license every file?

**A**: No, the LICENSE file at the repository root applies to all content unless specified otherwise. You can add license headers to individual files if needed.

---

## 📚 License Resources

- **CERN-OHL-S-2.0**: 
  - Full text: https://ohwr.org/cern_ohl_s_v2.txt
  - Information: https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2
- **GPL-3.0**: 
  - Full text: https://www.gnu.org/licenses/gpl-3.0.txt
  - Information: https://www.gnu.org/licenses/gpl-3.0.html
- **CC-BY-4.0**: 
  - Full text: https://creativecommons.org/licenses/by/4.0/legalcode
  - Information: https://creativecommons.org/licenses/by/4.0/

---

## ✅ Quick Reference

| Content Type | Recommended License | Download Link |
|--------------|---------------------|---------------|
| Hardware designs | CERN-OHL-S-2.0 | https://ohwr.org/cern_ohl_s_v2.txt |
| Software code | GPL-3.0 | https://www.gnu.org/licenses/gpl-3.0.txt |
| Documentation | CC-BY-4.0 | https://creativecommons.org/licenses/by/4.0/legalcode |

---

**Last Updated**: 2025-01-XX  
**Maintained by**: Wenzel-Lab

