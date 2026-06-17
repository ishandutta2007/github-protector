# 🛡️ GitHub Protector

![GitHub Protector Banner](assets/banner.svg)

[![PyPI version](https://img.shields.io/pypi/v/github-protector.svg)](https://pypi.org/project/github-protector/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/github-protector.svg)](https://pypi.org/project/github-protector/)
[![GitHub followers](https://img.shields.io/github/followers/ishandutta2007?label=Follow)](https://github.com/ishandutta2007)

**github-protector** is a lightweight, efficient CLI tool designed for developers and DevOps engineers to instantly secure their GitHub repository branches. With a single command, you can enforce industry-standard protection rules, ensuring your codebase remains robust and stable.

---

## 🚀 Key Features

- **⚡ Instant Protection:** Apply branch protection rules in seconds.
- **🛠️ Zero Config:** Automatically detects your repository, owner, and current user.
- **🛡️ Secure Defaults:** Enforces Pull Request reviews and minimum approval counts.
- **🔗 Flexible API:** Seamlessly integrates into your CI/CD pipelines.

---

## 📦 Installation

Install `github-protector` directly from PyPI using pip:

```bash
pip install github-protector
```

For local development and testing:

```bash
git clone https://github.com/ishandutta2007/github-protector.git
cd github-protector
pip install -e .
```

---

## 🛠️ Usage

### 1. Simple Mode (Auto-detection)
Run this inside any git repository. It will automatically detect the owner, repo, and target `main` branch.

```bash
github-protect
```

### 2. Explicit Mode
Provide specific details for fine-grained control:

```bash
github-protect --token YOUR_GITHUB_TOKEN --username ishandutta2007 --repo MyRepo --branch develop
```

### 3. Help & Options
Explore all available flags:

```bash
github-protect --help
```

---

## ⚙️ Configuration

You can set up a `.env` file in your project root to avoid passing tokens every time:

```env
ADMIN_TOKEN=your_personal_access_token_here
```

---

## 🗺️ Project Structure

```text
github-protector/
├── assets/                  # Visual assets and banners
├── github_protector/
│   ├── __init__.py
│   └── cli.py               # Core CLI logic
├── pyproject.toml           # Package metadata
└── README.md                # Documentation
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or find a bug, please open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` (if available) or the badge above for more information.

---

<p align="center">
  Developed with ❤️ by <a href="https://github.com/ishandutta2007">Ishan Dutta</a>
</p>
