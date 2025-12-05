# Quick Start Guide

**For hardware people new to software development**

This guide explains the basics in simple terms, without assuming prior software knowledge.

---

## 🤔 Common Questions

### What is `pyproject.toml`?

**Simple answer:** It's a configuration file that tells Python what your project needs.

**Think of it like:** A recipe card that lists all the ingredients (dependencies) your code needs to run.

**Do you need it?** Not really! You can use a simpler `requirements.txt` file instead:

```text
# requirements.txt (much simpler!)
numpy
pyvisa
pyqt5
```

**When to use `pyproject.toml`:**
- Your project is getting complex
- You want to configure multiple tools in one place
- You're comfortable with Python packaging

**When to use `requirements.txt`:**
- You're just starting out
- Your project is simple
- You want something easy to understand

**Recommendation:** Start with `requirements.txt`. You can always switch later!

---

### What is the `src/` folder?

**Simple answer:** It's a folder that holds all your Python code.

**What `src` means:** "Source" - it's where your source code lives.

**Why use it?** It's a Python best practice that helps avoid confusion, but it's **not required**.

**Think of it like:** Organizing your workshop - you could put tools directly on the bench, or in a toolbox. Both work, but the toolbox keeps things organized.

**Do you need it?** No! You can put your code directly in the root:

```
# Simple structure (no src/ folder)
instrument-name/
├── instrument/          # Your Python code here
│   ├── devices/
│   └── ...
└── tests/
```

**When to use `src/`:**
- Your project is getting large
- You want to follow Python best practices
- You're comfortable with Python packaging

**When to skip `src/`:**
- You're just learning
- Your project is small
- You want the simplest structure possible

**Recommendation:** Skip it for now! Start simple. You can always add it later if needed.

---

## 📁 Simple Project Structure

Here's the **simplest** structure that works perfectly fine:

```
your-instrument/
├── README.md
├── instrument-config.yaml
├── requirements.txt              # Simple list of dependencies
├── instrument/                   # Your Python code (no src/ needed!)
│   ├── __init__.py
│   ├── devices/
│   │   ├── base.py
│   │   └── simulated_.py
│   ├── controllers/
│   ├── gui/
│   └── main.py
└── tests/
```

**That's it!** No `src/`, no `pyproject.toml` - just the essentials.

---

## 🚀 Getting Started

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

## 📚 When to Use What

### Use Simple Structure When:
- ✅ You're learning Python
- ✅ Your project is small (< 10 files)
- ✅ You want to understand everything
- ✅ You're working alone or in a small team

### Use Advanced Structure When:
- ✅ Your project is getting large
- ✅ You're distributing your code to others
- ✅ You want to follow Python best practices
- ✅ You're comfortable with Python packaging

---

## 🎯 Key Takeaway

**Start simple!** You don't need `src/` or `pyproject.toml` to write good code. These are "nice to have" features that help as projects grow, but they're not required.

**The most important things:**
1. ✅ Your code works
2. ✅ It's organized in folders
3. ✅ Others can understand it
4. ✅ You can test it

Everything else is optional!

---

## 📖 Learn More

- **[INSTRUMENT_SOFTWARE_GUIDE.md](INSTRUMENT_SOFTWARE_GUIDE.md)** - Complete guide (explains why we use `src/` and `pyproject.toml`)
- **[example-structure/](example-structure/)** - See a complete example

---

**Remember:** There's no "wrong" way to structure a small project. Start simple, and add complexity only when you need it!

