# github_protector


Project Structure:

```
github-protector/
   ├── pyproject.toml           # Package metadata and entry points
   ├── github_protector/
   │   ├── __init__.py
   │   └── cli.py               # Main CLI logic
   └── .env                     # Your local environment file
```

Installation:
To install it locally in editable mode (so changes reflect immediately):
```
   pip install -e .
```

Usage:
Once installed, you can run it from anywhere:

1. Using defaults (from .env and git):
   `github-protect`
2. Providing explicit arguments:
   `github-protect --token YOUR_TOKEN --username ishandutta2007 --repo MyRepo --branch main`
3. View Help:
   `github-protect --help`

To Upload to PyPI:
If you want to share this on PyPI, follow these steps:

1. Build the package:
```
   pip install build
   python -m build
```

2. Upload using Twine:
```
   pip install twine
   python -m twine upload dist/*
```
   