# AI-Diet

`AI-Diet` is a lightweight Python developer library designed to solve the "AI Context Window" repetition problem. When using tools like ChatGPT, Claude, or Copilot, AI models frequently repeat whole blocks of utility functions across different codebase files. 

This package parses your project directory's Abstract Syntax Trees (AST) to uncover identical logic structures, helping you slim down generated code bloat.

## Installation

Install from GitHub:
```bash
pip install git+https://github.com/vd1686/ai-diet.git
```

Or from PyPI (once published):
```bash
pip install ai-diet
```

## Quick Start

```python
import ai_diet

# Scan a project directory
ai_diet.scan_for_ai_bloat("./my_project")
```
