# Quick Start Guide

**Beginner-friendly guide for hardware people new to software development**

This guide explains the basics in simple terms, without assuming prior software knowledge.

---

## Simple Project Structure

Here's the structure we use - it's designed to be simple and accessible:

```
your-instrument/
├── README.md
├── instrument-config.yaml
├── requirements.txt              # Simple list of dependencies
├── instrument/                   # Your Python code
│   ├── __init__.py
│   ├── devices/
│   │   ├── base.py
│   │   └── simulated_.py
│   ├── controllers/
│   ├── gui/
│   └── main.py
└── tests/
```

**That's it!** Just the essentials - simple and clear.

---

## Getting Started

### Step 1: Create Your Project

```bash
# Create a new folder
mkdir my-instrument
cd my-instrument

# Create basic structure
mkdir instrument tests
touch instrument/__init__.py
touch requirements.txt
touch instrument-config.yaml
```

### Step 2: Add Dependencies

Create `requirements.txt`:

```text
numpy
pyvisa
pyqt5
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start Coding

Create your first file: `instrument/main.py`

```python
# instrument/main.py
print("Hello from my instrument!")
```

Run it:

```bash
python -m instrument.main
# Or: python instrument/main.py
```

---

## Key Takeaway

**Start simple!** This structure is designed to be beginner-friendly and accessible for interdisciplinary teams.

**The most important things:**
1. Your code works
2. It's organized in folders
3. Others can understand it
4. You can test it

---

## Learn More

- **[instrument-software-guide.md](instrument-software-guide.md)** - Complete guide
- **[example-structure/](example-structure/)** - See a complete example

---

**Remember:** There's no "wrong" way to structure a small project. Start simple, and add complexity only when you need it!
