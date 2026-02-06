# Automation File Sorter (CLI)

This project is part of my **Dev Journey**, a structured, project-based exploration
of different areas of software development.

It focuses on building a **safe, practical command-line automation tool**
that organizes files in a directory based on their file extensions.

---

## Project goals

- Understand how real-world automation scripts are designed
- Learn how to safely manipulate the filesystem using a CLI tool
- Practice separating analysis, decision-making, and execution logic
- Handle edge cases and user input validation
- Build a reusable, idempotent developer tool

---

## Features

- Sorts files by their extension (e.g. `.pdf`, `.jpg`, `.txt`)
- Automatically creates destination folders when needed
- Supports files without extensions via a configurable `others` folder
- Dry-run mode to preview actions without modifying the filesystem
- Verbose mode for detailed execution logs
- Detects and skips conflicts safely
- Safe to run multiple times on the same directory

---

## Usage

Run the script from the command line:

```bash
python sorter.py <directory_path> [options]
```

### Options
- `--dry-run`

    Preview actions without creating folders or moving files
- `-v`, `--verbose`

    Display detailed output for each step and action
- `others-folder <name>`

    Folder name used for files without extensions (default: others)

### Examples

```bash
# Preview actions
python sorter.py ./downloads --dry-run -v

# Sort files normally
python sorter.py ./downloads

# Verbose execution
python sorter.py ./downloads -v

```

---

## How it works
1. Command-line arguments are parsed and validated
2. The target directory is scanned (non-recursive)
3. Files are analyzed and classified by extension
4. Required destination directories are identified
5. Actions are generated (create directories, move files)
6. Conflicts are detected before execution
7. Actions are executed safely
8. A summary is displayed at the end

---

## Project structure
```bash
file_sorter/
├── sorter.py                # CLI entry point
├── analysis.py              # Filesystem analysis & action planning
├── executor.py              # Action execution layer
├── actions.py               # Action data model
├── processed_files.py       # File classification logic
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── tests/
    └── test_directory_template/
        ├── README.md
        └── .gitkeep
```

---

## Testing
A reusable test directory template is provided in:
```bash
tests/test_directory_template/
```
This directory can be copied and populated manually to simulate real-world
scenarios (conflicts, existing folders, mixed file types, etc.).

The script is designed to be tested safely using `--dry-run`.

---

## Technologies used
- Python 3
- Python standard libraries only
- argparse
- os / shutil for filesystem operations

---

## Key concepts practiced
- Automation scripting
- Command-line interface design
- Filesystem traversal and manipulation
- Defensive programming
- Separation of concerns
- Idempotent script design

---

## Scope and limitations
- Non-recursive directory processing
- No file renaming or content inspection
- No external dependencies
- CLI-only (no GUI)
- Designed for learning and daily-use automation

---

## What I learned
- How to think in terms of automation rather than applications
- How to design scripts that are safe to rerun
- How to detect and handle filesystem conflicts
- How to structure a CLI tool cleanly
- How small utilities can deliver real productivity gains

---

## Versioning

This project follows **Semantic Versioning**.

Current version: **v1.0.0**

---

## How this fits into my dev journey
This project represents my first automation-focused CLI tool.
It bridges the gap between learning Python fundamentals and building
useful, real-world developer utilities.

it serves as a foundation for future projects involving:
- scripting
- system tools
- automation pipelines
- CLI application design