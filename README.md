# Log Analyzer with Percentage Metrics

### 1. What it does
This program parses a log file, filters out unusable lines, and calculates the top occurring log entries along with their percentage frequencies.

### 2. Why it exists
Log files are messy, filled with blank lines, and stack traces that make manual inspection impossible. This tool was built to quickly find the most common events and determine their relative impact on system activity.

### 3. What you need first
* Python 3.x installed on your machine
* A log file to parse (e.g., `mylog.log`) containing structured timestamps or events

### 4. How to run it
Run the script from your terminal using the following copy-pasteable command layout:

python3 summary.py mylog.txt 4

* `summary.py`: The main program script.
* `mylog.log`: The input log file path to analyze.
* `4`: The field index/position within the log line to count on.

### 5. What the output looks like
Lines total: 738
Skipped 43 lines that didn't fit the expected format.

--- TOP RESULTS WITH PERCENTAGES ---
ERROR_TIMEOUT: 250 occurrences (36.0%)
INFO_SUCCESS: 210 occurrences (30.2%)
WARN_LATENCY: 145 occurrences (20.9%)
ERROR_AUTH: 90 occurrences (12.9%)

### 6. What it can't do yet
* It cannot handle log files where the target field changes column index position from line to line.
* It cannot automatically identify or visualize trend patterns over time across multiple separate files.
