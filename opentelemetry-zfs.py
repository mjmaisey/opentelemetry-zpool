#!/usr/bin/python3

import subprocess
import json

# Execute the command-line tool and capture its output
command = "zpool list -H -p -o name,size,alloc,free"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Split the output into lines
lines = result.stdout.strip().split('\n')

# Process each line
for line in lines:
    # Split the line into columns
    columns = line.split()
    
    # Ensure we have the expected number of columns
    if len(columns) == 4:
        name, size, alloc, free = columns
        
        # Process the data as needed
        print(f"Name: {name}")
        print(f"Size: {size}")
        print(f"Allocated: {alloc}")
        print(f"Free: {free}")
        print("---")
    else:
        print(f"Skipping invalid line: {line}")