List Operations Example
Overview
This Python script demonstrates common list operations such as adding, inserting, extending, removing, sorting, and finding the index of an element.

The goal is to illustrate how Python's list methods work step-by-step.

Code Explanation
python
Copy
Edit
# Create an empty list
my_list = []

# Add elements using append()
my_list.append(10)   # [10]
my_list.append(20)   # [10, 20]
my_list.append(30)   # [10, 20, 30]
my_list.append(40)   # [10, 20, 30, 40]

# Insert an element at a specific position
my_list.insert(1, 15)  # [10, 15, 20, 30, 40]

# Extend the list with multiple elements
my_list.extend([50, 60, 70])  # [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element using pop()
my_list.pop()  # [10, 15, 20, 30, 40, 50, 60]

# Sort the list in ascending order
my_list.sort()  # [10, 15, 20, 30, 40, 50, 60]

# Find the index of a specific element
index_of_30 = my_list.index(30)  # 3

# Display the index
print(index_of_30)
Output
When run, the script prints:

Copy
Edit
3
This is because the value 30 is located at index 3 in the sorted list.

Key List Methods Used
append(item) → Adds an item to the end of the list.

insert(index, item) → Inserts an item at a given position.

extend(iterable) → Adds multiple items to the end of the list.

pop() → Removes and returns the last element.

sort() → Sorts the list in ascending order by default.

index(item) → Returns the index of the first occurrence of an item.
