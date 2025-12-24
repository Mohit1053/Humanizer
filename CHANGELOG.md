# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Web-based interface for easier usage
- Support for additional AI models
- Batch processing improvements
- More prompt variations

## [1.0.1] - 2024-12-24

### Fixed
- Removed all hardcoded user-specific paths
- Converted absolute paths to relative paths for portability
- Enhanced .gitignore to exclude generated output files

### Changed
- Updated all Python scripts to use relative file paths
- Made project fully portable and user-agnostic

### Security
- Ensured no sensitive information in repository
- Added proper .gitignore patterns for credentials

## [1.0.0] - 2024-12-24

### Added
- Initial release of AI Humanizer
- Core humanization engine with optimized prompts
- Support for CSV batch processing
- Multiple testing scripts for verification
- Comprehensive README with usage instructions
- MIT License
- Requirements file with all dependencies

### Features
- `humanize_v2.py` - Main production script with optimized prompts
- `humanize_csv.py` - Legacy version with alternative approaches
- `test_humanizer.py` - Quick 5-sample testing script
- `generate_test_samples.py` - Generate formatted test samples
- `generate_samples.py` - Alternative sample generator
- `optimize_prompts.py` - Prompt optimization experiments
- `quick_test.py` - Quick testing utilities
- `single_test.py` - Single text transformation testing

### Documentation
- Comprehensive README.md with badges and examples
- TEST_SAMPLES_READY.md with pre-generated test samples
- Clear installation and usage instructions
- Troubleshooting guide

### Technical
- Llama3 8B model integration via Ollama
- Progress tracking with tqdm
- Resume capability for interrupted processing
- Rate limiting to prevent API overload
- Configurable batch processing

---

## Release Notes

### Version Naming
- **Major** (x.0.0): Breaking changes
- **Minor** (0.x.0): New features, backward compatible
- **Patch** (0.0.x): Bug fixes, minor improvements

### Categories
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements
