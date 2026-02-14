# 🔥 1. Find First Non-Repeating Character (Memory + Edge Cases)
# Problem

# Return the first non-repeating character in a string. If none, return None.

Optimized Solution (O(n), minimal passes)
def first_unique_char(s: str):
    if not s:
        return None
    
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    for ch in s:
        if freq[ch] == 1:
            return ch
    
    return None

# What Interviewer Checks

# Dictionary usage

# Handling empty string

# Avoiding nested loops (O(n²) trap)

# Clean iteration logic



# 🔥 2. Remove Duplicates from List (In-Place vs Extra Memory)
# Problem

# Remove duplicates from a list while preserving order.

# Efficient (O(n), O(n) space)
# def remove_duplicates(arr):
#     seen = set()
#     result = []
    
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
    
#     return result

# Advanced (In-place for sorted list – O(1) space)
# def remove_duplicates_sorted(arr):
#     if not arr:
#         return 0
    
#     write = 1
#     for read in range(1, len(arr)):
#         if arr[read] != arr[read - 1]:
#             arr[write] = arr[read]
#             write += 1
    
#     return write

# What This Tests

# Set usage

# Space-time tradeoff awareness

# Two-pointer optimization

# Mutability understanding




# 🔥 3. Check If Two Strings Are One Edit Away (Edge Case Heavy)
# Problem

# Check if two strings are at most one edit away (insert/delete/replace).

# def one_edit_away(s1, s2):
#     if abs(len(s1) - len(s2)) > 1:
#         return False
    
#     if len(s1) > len(s2):
#         s1, s2 = s2, s1
    
#     i = j = 0
#     found_difference = False
    
#     while i < len(s1) and j < len(s2):
#         if s1[i] != s2[j]:
#             if found_difference:
#                 return False
#             found_difference = True
            
#             if len(s1) == len(s2):
#                 i += 1
#         else:
#             i += 1
        
#         j += 1
    
#     return True

# What It Tests

# Pointer logic

# Handling unequal lengths

# Edge case control flow




# 🔥 4. Implement LRU Cache (Optimization + Data Structures)

# This question separates average from strong candidates.

# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
        
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)

# Tests

# O(1) operations

# Understanding of ordered hashing

# Memory control via capacity




# 🔥 5. Generator vs List (Memory Optimization)
# Problem

# Return squares of numbers from 1 to n.

# Memory Heavy (Bad for large n)
# def squares_list(n):
#     return [i*i for i in range(n)]

# Memory Efficient (Lazy Evaluation)
# def squares_generator(n):
#     for i in range(n):
#         yield i*i

# Why This Is Powerful

# If n = 10^8, list crashes memory.
# Generator uses constant memory.

# Interview Talking Point

# "Generators are preferable for streaming/ETL pipelines or large datasets to avoid memory exhaustion."

# That’s strong engineering thinking — especially relevant to your data engineering + AI background.




# 🔥 6. Deep Copy vs Shallow Copy (Classic Trap)
# import copy

# a = [[1, 2], [3, 4]]

# b = a[:]                # Shallow copy
# c = copy.deepcopy(a)    # Deep copy

# Interview Follow-up

# Modify a[0][0] and observe behavior.

# Tests:

# Object references

# Mutability

# Memory model understanding




# 🔥 7. Optimize Word Frequency Counter (Streaming Style)
# def word_frequency(stream):
#     freq = {}
    
#     for line in stream:
#         for word in line.split():
#             freq[word] = freq.get(word, 0) + 1
    
#     return freq


# Talking Point:

# Works for file streams

# Avoids loading full file into memory

# Scalable approach
