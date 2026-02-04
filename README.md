# File Sorter Script

This project is part of my Dev Journey, a structured, project-based exploration
of the main types of software development.

It focuses on building a simple yet practical automation tool to organize files on a local filesystem.

---

## Project goals

- Understand what a real-world automation script is and how it is structured
- Learn how to safely manipulate the filesystem using a CLI tool
- Practice writing a useful, reusable script rather than a purely academic exercise
- Gain confidence in handling edge cases and user input validation

---

## Features

- Sorts files in a given directory by their file extension
- Automatically creates subfolders for each detected extension
- Moves files into the appropriate subfolder
- Supports a dry-run mode to preview actions without modifying anything
- Provides clear terminal output for user feedback

---

## Usage

The script is executed from the command line and takes a directory path as input.

Typical usage examples:
- Sort files in a directory by extension
- Preview what would happen without moving any files
- Display detailed information about each action performed

---

## How it works

1. The script reads and validates command-line arguments
2. It scans the target directory and identifies files (excluding subdirectories)
3. Each file’s extension is analyzed and normalized
4. A target folder is determined for each file
5. Required folders are created if they do not already exist
6. Files are either moved or listed, depending on the execution mode
7. A summary of the operation is displayed at the end

---

## Project structure

```bash
file_sorter/
├── README.md
├── sorter.py
├── requirements.txt
└── examples/
    └── sample_folder/
```

---

## Technologies used

- Python 3
- Python Standard Library only
- argparse for CLI handling
- OS and filesystem utilities

---

## Key concept practiced

- Automation scripting
- Command-line interface design
- Filesystem traversal and manipulation
- Defensive programming and error handling
- Designing safe, repeatable developer tools

---

## Scope & limitations

- The script only processes files in a single directory (non-recursive)
- No advanced file renaming is performed
- No graphical interface
- No external dependencies
- Designed for learning and daily-use automation, not large-scale file systems

---

## What I learned

- How to think in terms of automation rather than application development
- How to design a script that is safe to run multiple times
- The importance of separating analysis, decision-making, and execution
- How small tools can provide real productivity gains

---

## Versioning

v1.0 — Initial implementation: file sorting by extension with CLI support

---

## How this fits into my dev journey

This project represents my first step into automation development, following a CLI-based project.
It helped me shift from writing programs that demonstrate concepts to scripts that solve real problems,
laying the foundation for more advanced automation, scripting, and system-level projects.