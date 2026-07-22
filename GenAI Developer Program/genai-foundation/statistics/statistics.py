# Python Set is a collection which is unordered, unchangeable*, and unindexed.
# *Unchangeable, meaning that we cannot change the items after the set has been created, but we can add new items.
# A set cannot have duplicate items. If you try to add a duplicate item, it will be ignored.
# Sets are unordered, meaning that the items do not have a defined order, and you cannot access them by index.
# Sets are unindexed, meaning that you cannot access items in a set by referring to an index or a key.But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword
# Set importance in ai and ml is that it can be used to store unique values, which is often useful in tasks such as feature selection, data preprocessing, and handling categorical data. Sets can also be used to perform operations like union, intersection, and difference, which can help in analyzing and manipulating data efficiently.
words = {"ai", "ml", "ai"}
print(words)

# Real time example of set in ai and ml
# Let's say we have a dataset of customer reviews for a product, and we want to extract
unique_features = {
    "feature1",
    "feature2",
    "feature3",
    "feature1",
}  # Duplicate feature will be ignored
print(unique_features)

# please teach what all python concepts are used in this code and how they are used in ai and ml with real time examples.
# Please teach all concepts in detail with python real time ai implmentataion with examples
# Please teach
# NumPy is a powerful library in Python for numerical computing. It provides support for arrays, matrices, and a wide range of mathematical functions to operate on these data structures. In AI and ML, NumPy is widely used for data manipulation, preprocessing, and performing mathematical operations on datasets.
import numpy as np

# Creating a 2D array (matrix)
# NumPy arrays are the backbone for scientific computing in Python because they’re way faster than regular Python lists and you can do whole-matrix operations in one go.
# np.allows us to create arrays of any dimension, and we can perform operations on them efficiently. In AI and ML, we often deal with large datasets, and using NumPy arrays allows us to manipulate and analyze this data effectively.
# add conditional check before creating the array to ensure that the input data is valid and can be converted into a NumPy array. This is important in AI and ML applications where data integrity is crucial for model training and performance.
# Simple Example of np.allows    ?


# do a condition check before reading or using the matrix. That’s called “validation” or a “guard clause”.
# Check the NumPy array right after creating it, before you access elements


# ============================================================
# TOPIC 9: Python Set — Unique Values Only
# Duplicate values are automatically removed.
# Useful in ML for unique class labels or vocabulary tokens.
# ============================================================
unique_ids = {4, 2, 3, 3}
print(unique_ids)

# ============================================================
# TOPIC 10: Python List — Preserves Duplicates & Order
# Unlike sets, lists keep all values including duplicates.
# ============================================================
list = [1, 2, 3, 3]
print(list)

# Statistics

# Mean
v = np.array([5, 10, 15, 20])

print(v)

print("Mean", v.mean())

# Median

median = np.median(v)
print("Median:", median)

# Mode
import numpy as np
from scipy import stats

v = np.array([5, 20, 5, 35, 5, 35, 35, 20, 20])
print(v)
mode_result = stats.mode(v, keepdims=True)

print("Mode:", mode_result.mode[0])


# MODE

# Definition:
# Mode is the value or values that occur most frequently in a dataset.

# Key Points:
# • Mode represents the highest frequency occurrence.
# • A dataset can have one mode, multiple modes, or no mode.
# • Mode can be used with numbers, strings, categories, classes, defect types, browser names, etc.

# Examples:

# Dataset:
# [1, 2, 2, 3, 4]

# Frequency:
# 1 → 1
# 2 → 2
# 3 → 1
# 4 → 1

# Mode = 2


# Dataset:
# ["Chrome", "Firefox", "Chrome", "Edge"]

# Frequency:
# Chrome  → 2
# Firefox → 1
# Edge    → 1

# Mode = Chrome


# Real-world Uses:
# • Most common browser used by customers
# • Most common defect category
# • Most purchased product
# • Most frequent AI prediction class
# • Most common error message

# **BIMODAL DATASET

# Definition:
# A bimodal dataset is a dataset that contains exactly two modes.

# Key Points:
# • Two values share the highest frequency.
# • Both values are considered modes.
# • The values can be numbers, strings, categories, or classes.

# Numeric Example:

# Dataset:
# [5, 10, 15, 20, 5, 10]

# Frequency:
# 5  → 2
# 10 → 2
# 15 → 1
# 20 → 1

# Modes = 5, 10

# Dataset Type = Bimodal


# String Example:

# Dataset:
# ["Chrome", "Firefox", "Chrome", "Firefox", "Edge"]

# Frequency:
# Chrome  → 2
# Firefox → 2
# Edge    → 1

# Modes = Chrome, Firefox

# Dataset Type = Bimodal


# AI Example:

# Predictions:
# Cat, Dog, Cat, Dog, Cat, Dog

# Frequency:
# Cat → 3
# Dog → 3

# Modes = Cat, Dog

# Dataset Type = Bimodal


# Classification of Datasets:

# Unimodal  → One mode
# Example: [1, 2, 2, 3]

# Bimodal   → Two modes
# Example: [5, 10, 5, 10, 20]

# Multimodal → More than two modes
# Example: [1, 1, 2, 2, 3, 3]


# Interview Definition:

# Mode:
# "The value or values that occur most frequently in a dataset."

# Bimodal Dataset:
# "A dataset having exactly two modes, where two values share the highest frequency."
# But in AI, we usually need one final prediction.

# So the AI system applies a tie-breaking rule to choose the final result.


# **Counter
# Here are complete, interview-friendly Python programs for each real-world use case.Prgrams
# Exaple 1. Most Common Browser Used by Customers

from collections import Counter

browsers = ["Chrome", "Firefox", "Chrome", "Edge", "Chrome"]
Counter(browsers)
