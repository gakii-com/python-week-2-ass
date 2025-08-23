# Create an empty list
my_list = []

# Append 10 to the list → [10]
my_list.append(10)

# Append 20 to the list → [10, 20]
my_list.append(20)

# Append 30 to the list → [10, 20, 30]
my_list.append(30)

# Append 40 to the list → [10, 20, 30, 40]
my_list.append(40)

# Insert 15 at index 1 → [10, 15, 20, 30, 40]
my_list.insert(1, 15)

# Extend the list with [50, 60, 70] → [10, 15, 20, 30, 40, 50, 60, 70]
my_list.extend([50, 60, 70])

# Remove and return the last element (70) → [10, 15, 20, 30, 40, 50, 60]
my_list.pop()

# Sort the list in ascending order (already sorted here) → [10, 15, 20, 30, 40, 50, 60]
my_list.sort()

# Find the index of value 30 → returns 3
index_of_30 = my_list.index(30)

# Print the index of 30 → 3
print(index_of_30)

