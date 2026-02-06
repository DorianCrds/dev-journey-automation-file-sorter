# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project follows Semantic Versioning.

---

## [Unreleased]

### Planned
- Unit tests
- Recursive directory support (optional)
- Optional overwrite / force flag
- Config file support
- Packaging as an installable CLI command

---

## [v1.0.0] – Initial stable release

### Added
- Command-line interface using argparse
- Directory validation and normalization
- File analysis and classification by extension
- Automatic creation of required directories
- File movement execution layer
- Dry-run mode for safe previews
- Verbose mode for detailed logs
- Conflict detection to prevent overwrites
- Reusable test directory template

### Technical details
- Clear separation between:
  - analysis (decision-making)
  - execution (filesystem operations)
- Action-based execution model
- Defensive error handling
- Standard library only

### Notes
- Non-recursive by design
- Safe to run multiple times on the same directory
- Designed as a learning-focused automation project
