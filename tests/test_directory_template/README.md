# Test Directory Template

This directory is a template used to manually test the file sorter.

Expected test cases:
- files with extensions (pdf, txt, jpg)
- files without extensions
- hidden files (.gitignore)
- existing directories
- conflict scenarios

You can populate a test directory with any files to test the sorter behavior using the following commands :

- On Linux / macOS :
```bash
touch report.pdf notes.txt image.jpg README archive.tar.gz
touch .gitignore
```

- On Windows (PowerShell) :
```bash
foreach ($file in "report.pdf","notes.txt","image.jpg","README","archive.tar.gz") {
    New-Item $file
}

New-Item .gitignore
```