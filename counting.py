best_key = " "
best_count = -1

second_best_key = " "
second_best_count = -1

for key, count in counts:
    if counts[key] > best_count:

        second_best_key = best_key
        second_best_count = best_count

        best_key = key
        best_count = counts[key]

print("1st:", best_key, best_count)

print("2nd:", second_best_key, second_best_count)