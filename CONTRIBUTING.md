# Contributing to AI Humanizer

Thank you for your interest in contributing to AI Humanizer! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### 1. Fork the Repository
1. Fork the repository to your GitHub account
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Humanizer.git
   cd Humanizer
   ```

### 2. Set Up Development Environment
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Ollama and pull the required model:
   ```bash
   ollama pull llama3:8b
   ```

### 3. Create a Branch
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 4. Make Your Changes
- Write clean, readable code
- Follow Python best practices (PEP 8)
- Use relative paths (never hardcode user-specific paths)
- Comment complex logic
- Test your changes thoroughly

### 5. Test Your Changes
Before submitting, test your changes:
```bash
python test_humanizer.py
```

### 6. Commit Your Changes
Follow conventional commit format:
```bash
git commit -m "feat: add new prompt optimization"
git commit -m "fix: resolve CSV encoding issue"
git commit -m "docs: update installation instructions"
git commit -m "chore: cleanup temporary files"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style/formatting
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### 7. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 8. Submit a Pull Request
1. Go to the original repository
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill out the PR template with:
   - Clear description of changes
   - Related issue number (if applicable)
   - Testing performed
   - Screenshots (if applicable)

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows project style guidelines
- [ ] All tests pass locally
- [ ] No hardcoded paths or sensitive information
- [ ] Documentation updated (if needed)
- [ ] Commit messages follow conventional format
- [ ] Code has been self-reviewed

### PR Review Process
1. Maintainers will review your PR within 2-3 days
2. Address any requested changes
3. Once approved, your PR will be merged

## 🐛 Reporting Bugs

When reporting bugs, please include:
- Detailed description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, Ollama version)
- Error messages or logs
- Screenshots (if applicable)

Use the [Issue Template](.github/ISSUE_TEMPLATE.md) when creating issues.

## 💡 Feature Requests

We welcome feature requests! Please:
- Check existing issues first to avoid duplicates
- Clearly describe the feature and its benefits
- Provide use cases
- Suggest implementation approach (if you have ideas)

## 🎯 Areas for Contribution

Looking for ways to contribute? Consider:

### High Priority
- **Prompt optimization** - Better prompts for lower AI detection
- **Performance improvements** - Faster processing
- **Error handling** - More robust error messages
- **Documentation** - Tutorials, examples, troubleshooting guides

### Medium Priority
- **New features** - Batch processing improvements, web UI
- **Testing** - Unit tests, integration tests
- **Code quality** - Refactoring, type hints

### Good First Issues
- Documentation improvements
- Bug fixes
- Adding examples
- Improving error messages

## 📝 Code Style Guidelines

### Python Style
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Maximum line length: 127 characters
- Use type hints where appropriate

### File Structure
```python
"""
Module description
"""
import standard_library
import third_party_libs

# Constants
CONSTANT_NAME = "value"

# Functions
def function_name():
    """Function docstring"""
    pass
```

### Best Practices
- Use relative paths only
- No hardcoded configuration
- Include error handling
- Add progress indicators for long operations
- Log important actions

## 🔐 Security

If you discover a security vulnerability:
1. **DO NOT** open a public issue
2. Email the maintainer directly
3. Include detailed information about the vulnerability
4. Allow time for a fix before public disclosure

## 📜 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Unprofessional conduct

## 📞 Getting Help

Need help? You can:
- Open an issue with the "question" label
- Check existing documentation
- Review closed issues for similar problems

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for making AI Humanizer better! 🚀

---

**Questions?** Open an issue or reach out to the maintainers.
