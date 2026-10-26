from collections import Counter

counts = Counter()

# Read your log file and populate the counter
try:
    with open("test_file.txt", "r") as file:
        for line in file:
            # Example: treating each line or a specific part of the line as a key
            key = line.strip() 
            if key:
                counts[key] += 1
except FileNotFoundError:
    print("test_file.txt")

best_key = None
best_count = -1

second_best_key = None
second_best_count = -1

for key, count in counts.items():
    if count > best_count:
        second_best_key = best_key
        second_best_count = best_count

        best_key = key
        best_count = count
    elif count > second_best_count:
        second_best_key = key
        second_best_count = count

total_valid_lines = sum(counts.values())

print("\n--- TOP RESULTS WITH PERCENTAGES ---")
for key, count in counts.most_common(5):
    percentage = (count / total_valid_lines) * 100 if total_valid_lines > 0 else 0
    print(f"{key}: {count} occurrences ({percentage:.1f}%)")

print("1st:", best_key, best_count)
print("2nd:", second_best_key, second_best_count)





# best_key = " "
# best_count = -1

# second_best_key = " "
# second_best_count = -1
# counts = Counter()
# def Counter():
#     return {}

# Counter()
# for key, count in counts:
#     if counts[key] > best_count:

#         second_best_key = best_key
#         second_best_count = best_count

#         best_key = key
#         best_count = counts[key]

# # Assuming total_valid_lines is calculated while reading the file
# print("\n--- TOP RESULTS WITH PERCENTAGES ---")
# for key, count in top_five:
#     percentage = (count / total_valid_lines) * 100
#     print(f"{key}: {count} occurrences ({percentage:.1f}%)")

# print("1st:", best_key, best_count)

# print("2nd:", second_best_key, second_best_count)