# Python Log Analyzer

## Project Overview
A Python-based security log analyzer designed
to detect suspicious login activity and
potential brute-force attacks.

## Features
- Analysis of authentication logs.
- Failed login counting.
- User-based login activity tracking.
- Detection of potential brute-force attacks.
- Timestamp parsing and chronological sorting.
- Invalid log entry handling.
- Missing and empty file handling.

## Detection Logic
The program generates a warning when a single
user has at least five failed login attempts
within a 300-second time window.

## Requirements
- Python 3
- No external libraries required.

## How to Run
Open a terminal in the project directory:

python main.py

## Project Files
- main.py - Main analysis script.
- sample.log - Sample authentication logs.
- test_attacks.log - Attack detection test data.
- test_empty.log - Empty file test.
- README.md - Project documentation.

## Limitations
- Supports a specific log format.
- Reads logs from a predefined file.
- Detects suspicious activity, not confirmed attacks.

## Future Improvements
- Custom detection thresholds.
- IP address analysis.
- Command-line arguments.
- Automated testing.

## Purpose
This project was developed as a learning
project focused on Python, cybersecurity,
log analysis and Blue Team fundamentals.