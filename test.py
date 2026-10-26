import os
print(os.getcwd())

skipped_count = 0
total_lines = 0
EXPECTED_LENGTH = 10  # Change this to whatever your program expects

with open("test_file.txt", "r") as file:
    for line in file:
        total_lines += 1
        clean_line = line.strip() # Removes newline characters (\n)
        
        # 1. Check for blank lines OR 2. Check for lines shorter than expected
        if clean_line == "" or len(clean_line) < EXPECTED_LENGTH:
            skipped_count += 1
            continue # Skip processing this line and go to the next
            
        # ... your normal program logic for good lines goes here ...

print(f"Lines total: {total_lines}")
print(f"Skipped {skipped_count} lines that didn't fit the expected format.")