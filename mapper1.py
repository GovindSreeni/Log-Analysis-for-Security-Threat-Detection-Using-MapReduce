#!/usr/bin/env python3
import sys

# Function to determine if a status code is success or failure
def is_success(status_code):
    return status_code < 400

# Read each line from standard input
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) != 5:
        continue  # Skip if not a valid log line
    domain = parts[0]
    try:
        status_code = int(parts[4])
    except ValueError:
        continue  # Skip lines with invalid status codes
    
    # Output domain with success or failure status
    if is_success(status_code):
        print(f"{domain}\tsuccess")
    else:
        print(f"{domain}\tfailure")
