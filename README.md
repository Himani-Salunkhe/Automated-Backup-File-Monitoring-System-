# Automated Backup File Monitoring System

A Python automation utility that periodically scans a directory, identifies zero-byte files, removes them, and writes a scan report to a timestamped log file.

## Features

- Recursively scans directories and subdirectories
- Detects files with a size of `0` bytes
- Deletes empty files automatically
- Runs the scan every minute
- Creates a new timestamped log file for each scan
- Reports the total number of files scanned and empty files deleted
- Provides command-line help and usage information

## Project Structure

```text
Automated-Backup-File-Monitoring-System-/
├── DirectoryScannerEmptydeleteFinal.py  # Main directory scanner script
├── Requirement.txt                      # Project dependencies
├── Empty_Files/                         # Example files and utility scripts
├── Marvellous*.log                      # Generated scan logs
└── README.md
```

## Requirements

- Python 3
- [`schedule`](https://pypi.org/project/schedule/) package

Install the dependency:

```powershell
pip install schedule
```

## Usage

Run the script with an absolute directory path:

```powershell
python DirectoryScannerEmptydeleteFinal.py "C:\path\to\directory"
```

The script validates the path and then continuously checks the directory every minute.

Stop the program with `Ctrl+C`.

### Help

```powershell
python DirectoryScannerEmptydeleteFinal.py --h
```

### Usage information

```powershell
python DirectoryScannerEmptydeleteFinal.py --u
```

## How It Works

1. The script receives a directory path from the command line.
2. It validates that the path exists and is a directory.
3. Every minute, it recursively walks through the directory.
4. Files whose size is exactly `0` bytes are removed.
5. A log file named with the current date and time is created in the repository working directory.
6. The log records each scanned file, its size, and scan totals.

Example log name:

```text
MarvellousThu_Nov_26_23_31_17_2026.log
```

Log names are generated from the system timestamp, with spaces and colons replaced by underscores.

## Example Log

```text
----------------------------------------

Marvellous Automation Script
----------------------------------------

Files from the directory are:

----------------------------------------
E:\path\to\directory\file.txt : 28 bytes
E:\path\to\directory\empty.txt : 0 bytes
----------------------------------------
Total files scanned : 2
Total Empty files formed and deleted : 1
----------------------------------------
Log file gets created at : Thu Nov 26 23:31:17 2026
----------------------------------------
```

## Warning

The scanner permanently deletes zero-byte files from the supplied directory and all of its subdirectories. Back up important data and review the target directory before running the script.

## Author

Himani Ramesh Salunkhe