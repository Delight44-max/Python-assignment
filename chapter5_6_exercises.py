# Chapter 5 & 6 Coding Exercises Solutions

# ----------------------------
# Chapter 5 - Lists & Tuples
# ----------------------------

# 1) List statistics
def list_stats(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers)/len(numbers)
    }

nums = [5, 2, 9, 1, 7]
print("1) List statistics:", list_stats(nums))

# 2) Reverse a sequence
seq = [1, 2, 3, 4, 5]
print("2) Reverse sequence:", seq[::-1])

# 3) Student grades with tuples
students = [
    ("Alice", [85, 90, 92]),
    ("Bob", [70, 80, 75]),
    ("Carol", [88, 95, 100])
]
print("3) Student averages:")
for name, grades in students:
    avg = sum(grades) / len(grades)
    print(f"{name}: {grades} -> avg {avg:.2f}")

# 4) Matrix row & column sums
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("4) Matrix row sums:")
for i, row in enumerate(matrix):
    print(f"Row {i} sum:", sum(row))

print("Matrix column sums:")
for j in range(len(matrix[0])):
    col_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"Column {j} sum:", col_sum)

# 5) Remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(dict.fromkeys(nums))
print("5) Remove duplicates:", unique_nums)

# 6) Palindrome check
def is_palindrome(seq):
    return seq == seq[::-1]

print("6) Palindrome check:")
print(is_palindrome([1,2,3,2,1]))
print(is_palindrome("radar"))
print(is_palindrome("python"))

# ----------------------------
# Chapter 6 - Dictionaries & Sets
# ----------------------------

import re
from collections import defaultdict, Counter

# 7) Word count program
def word_count(text):
    words = re.findall(r"\b\w+\b", text.lower())
    counts = defaultdict(int)
    for w in words:
        counts[w] += 1
    return dict(counts)

print("7) Word count:", word_count("Hello hello test one two test"))

# 8) Letter frequency
text = "banana"
freq = Counter(text)
print("8) Letter frequency:", freq)

# 9) Invert a dictionary
phonebook = {"Alice": "123", "Bob": "456", "Carol": "789"}
inverted = {v:k for k,v in phonebook.items()}
print("9) Inverted dict:", inverted)

# 10) Common keys between dictionaries
d1 = {"a":1, "b":2, "c":3}
d2 = {"b":20, "c":30, "d":40}
common = d1.keys() & d2.keys()
print("10) Common keys:", common)

# 11) Vowel counter
text = "programming in python"
vowels = "aeiou"
counts = {v: text.count(v) for v in vowels}
print("11) Vowel counts:", counts)

# 12) Student gradebook with best student
grades = {
    "Alice": [90, 80, 85],
    "Bob": [70, 75, 65],
    "Carol": [100, 95, 98]
}
averages = {s: sum(g)/len(g) for s,g in grades.items()}
best_student = max(averages, key=averages.get)
print("12) Student averages:", averages)
print("Best student:", best_student, "with avg", averages[best_student])
