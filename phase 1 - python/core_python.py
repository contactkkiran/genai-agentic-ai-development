# List

from optparse import Values
from turtle import st

bounding_box = [10, 20, 100, 200]
# bounding_box[0] = 15  ❌ Error

# touple

bounding_box = (10, 20, 100, 200)
# bounding_box[0] = 15  # ✅ Works

# set

student1 = ("kiran", 46, "Hyderabad")

# Apply set
studentset = set(student1)
print(studentset)

# Aplly set to unhashable list
student2 = (["kiran", "Male"], 46, "Hyderabad")

# studentset = set(
#     student2
# )   Unhashable list ❌ Error . Set → hashable elements only. Tuple → OK only when all its contents are hashable.

# Enunerate

names = ["AI", "ML", "DL"]

for index, name in enumerate(names):
    print(index, name)


# dictionary

student = {"name": "kiran", "age": 45}
# keys()
print(student.keys())
# values
print(student.values())
# items
print(student.items())
for key, value in student.items():
    print(key, ": ", value)


# ===== COMPREHENSIVE PYTHON LOOPING TUTORIAL =====

print("\n" + "=" * 50)
print("1️⃣  FOR LOOP - Basic Iteration")
print("=" * 50)

# For loop iterating through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\n" + "=" * 50)
print("2️⃣  FOR LOOP with range()")
print("=" * 50)

# range(start, end, step)
# range(5) → 0, 1, 2, 3, 4
for i in range(5):
    print(f"Number: {i}")

# range(2, 8, 2) → 2, 4, 6
print("\nEven numbers from 2 to 8:")
for i in range(2, 8, 2):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("3️⃣  FOR LOOP with enumerate() - Index + Value")
print("=" * 50)

# enumerate() gives both index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

print("\n" + "=" * 50)
print("4️⃣  FOR LOOP with zip() - Multiple Lists")
print("=" * 50)

# zip() combines multiple lists
names_list = ["Alice", "Bob", "Charlie"]
ages_list = [25, 30, 35]

for name, age in zip(names_list, ages_list):
    print(f"{name} is {age} years old")

print("\n" + "=" * 50)
print("5️⃣  NESTED FOR LOOPS")
print("=" * 50)

# Loop inside a loop
print("Multiplication Table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # newline after inner loop

print("\n" + "=" * 50)
print("6️⃣  WHILE LOOP - Loop Until Condition is False")
print("=" * 50)

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print("\n" + "=" * 50)
print("7️⃣  BREAK - Exit Loop Early")
print("=" * 50)

# Break stops the loop immediately
for num in range(10):
    if num == 5:
        print(f"Found 5! Breaking out...")
        break
    print(num, end=" ")
print("\n(Loop stopped at 5)")

print("\n" + "=" * 50)
print("8️⃣  CONTINUE - Skip Current Iteration")
print("=" * 50)

# Continue skips to the next iteration
print("Printing even numbers only:")
for num in range(1, 11):
    if num % 2 != 0:  # if odd, skip
        continue
    print(num, end=" ")
print()

print("\n" + "=" * 50)
print("9️⃣  LOOP with ELSE - Executes if Loop Completes")
print("=" * 50)

# Else runs only if loop completes without break
for i in range(3):
    print(f"Loop iteration {i}")
else:
    print("✅ Loop completed successfully!")

print("\n" + "=" * 50)
print("🔟  LIST COMPREHENSION - Compact Loop")
print("=" * 50)

# List comprehension creates a new list in one line
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition - only even numbers squared
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

print("\n" + "=" * 50)
print("🔄  DICTIONARY LOOPING - Different Ways")
print("=" * 50)

person = {"name": "Kiran", "age": 45, "city": "Hyderabad"}

print("\nLoop through keys:")
for key in person:
    print(key, end=" ")
print()

print("\nLoop through values:")
for value in person.values():
    print(value, end=" ")
print()

print("\nLoop through items (key + value):")
for key, value in person.items():
    print(f"{key}: {value}")

print("\n" + "=" * 50)
print("💡  LOOP SUMMARY")
print("=" * 50)
