# Given an array nums and a target, return indices of two numbers that add up to the target.
# def two_sum(nums, target):
#     lookup = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in lookup:
#             return [lookup[diff], i]
#         lookup[num] = i
#     return []



# Problem: Check if two strings are anagrams.

# from collections import Counter

# def is_anagram(s, t):
#     return Counter(s) == Counter(t)

# First Non-Repeating Character
# from collections import OrderedDict

# def first_unique_char(s):
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char, 0) + 1

#     for i, char in enumerate(s):
#         if freq[char] == 1:
#             return i
#     return -1



# Reverse Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverse_list(head):
#     prev = None
#     curr = head
    
#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node
        
#     return prev
# Time: O(n)
# Space: O(1)


# Find Duplicate in List
# def find_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return num
#         seen.add(num)
# Time: O(n)
# Space: O(n)



# Merge Two Sorted Arrays
# def merge_sorted(arr1, arr2):
#     i = j = 0
#     result = []
    
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1
    
#     result.extend(arr1[i:])
#     result.extend(arr2[j:])
    
#     return result
# Time: O(n + m)



# Maximum Subarray (Kadane’s Algorithm)
# def max_subarray(nums):
#     max_sum = curr_sum = nums[0]
    
#     for num in nums[1:]:
#         curr_sum = max(num, curr_sum + num)
#         max_sum = max(max_sum, curr_sum)
        
#     return max_sum
# Time: O(n)



# 9. Valid Parentheses
# def is_valid_parentheses(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in mapping:
#             top = stack.pop() if stack else '#'
#             if mapping[char] != top:
#                 return False
#         else:
#             stack.append(char)
    
#     return not stack
# Time: O(n)



# Fibonacci (Iterative + Optimized)
# def fibonacci(n):
#     if n <= 1:
#         return n
    
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
# Time: O(n)
# Space: O(1)



# Detect Cycle in Linked List (Floyd’s Algorithm)
# def has_cycle(head):
#     slow = fast = head
    
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
        
#         if slow == fast:
#             return True
#     return False
