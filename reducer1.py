#!/usr/bin/env python3
import sys

# Initialize variables
current_domain = None
success_count = 0
failure_count = 0

# Read each key-value pair from standard input
for line in sys.stdin:
    domain, status = line.strip().split("\t")
    
    # If the domain changes (or first line), print the current counts and reset
    if current_domain and domain != current_domain:
        print(f"{current_domain}\tSuccessful connections: {success_count}\tFailed connections: {failure_count}")
        success_count = 0
        failure_count = 0

    # Set the new domain
    current_domain = domain

    # Update success or failure count
    if status == "success":
        success_count += 1
    else:
        failure_count += 1

# Output the last domain
if current_domain:
    print(f"{current_domain}\tSuccessful connections: {success_count}\tFailed connections: {failure_count}")
