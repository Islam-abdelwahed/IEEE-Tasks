# -----------------------------
# Problem 1
# -----------------------------
# Sum from 1 to n

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)


# -----------------------------
# Problem 2
# -----------------------------
# Second largest and second smallest (no built-in functions)

numbers = [4, 1, 7, 9, 3]

largest = smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

second_largest = None
second_smallest = None

for num in numbers:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num
    if num != smallest:
        if second_smallest is None or num < second_smallest:
            second_smallest = num

print("Second largest:", second_largest)
print("Second smallest:", second_smallest)


# -----------------------------
# Problem 3
# -----------------------------
# Two numbers that add to target

nums = [1, 4, 5, 6]
target = 5

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Indexes:", i, j)


# -----------------------------
# Problem 4
# -----------------------------
# Split strings into halves

words = ["apple", "Maid"]
first_half = []
second_half = []

for word in words:
    mid = len(word) // 2
    first_half.append(word[:mid])
    second_half.append(word[mid:])

print(first_half)
print(second_half)


# -----------------------------
# Problem 5
# -----------------------------
# Minimum distance between same numbers

nums = [2, 5, 3, 4, 5, 2]
min_distance = None

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            distance = j - i
            if min_distance is None or distance < min_distance:
                min_distance = distance

print("Minimum distance:", min_distance)


# -----------------------------
# Problem 6
# -----------------------------
# Output and explanation

z = 200 / 100
k = (1.1 + 2.2 != 3.3)
y = k and isinstance(z, int)

print("z =", z)
print("k =", k)
print("y =", y)


# -----------------------------
# Problem 7
# -----------------------------
print(round(6.5) - round(3.5) == 3)


# -----------------------------
# Problem 8
# -----------------------------
# Factorial using while loop

num = int(input("Enter a number: "))
factorial = 1
i = num

while i > 0:
    factorial *= i
    i -= 1

print(f"The factorial of {num} is {factorial}")


# -----------------------------
# Problem 9
# -----------------------------
# Break loop if input is 'q'

while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input == 'q':
        print("Loop exited!")
        break
    else:
        print("You entered:", user_input)
