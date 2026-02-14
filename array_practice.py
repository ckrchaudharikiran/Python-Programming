# Python program to find the largest number in an array 
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)


# Python program to store all even numbers from an array in another array
# import array as arr
# a = arr.array('i', [10,5,15,4,6,20,9])
# print (a)
# b = arr.array('i')
# for i in range(len(a)):
#    if a[i]%2 == 0:
#       b.append(a[i])
# print ("Even numbers:", b)



# Python program to find the average of all numbers in a Python array
# import array as arr
# a = arr.array('i', [10,5,15,4,6,20,9])
# print (a)
# s = 0
# for i in range(len(a)):
#    s+=a[i]
# avg = s/len(a)
# print ("Average:", avg)
# # Using sum() function
# avg = sum(a)/len(a)
# print ("Average:", avg)



# Python program find difference between each number in the array and the average of all numbers

# Python program to convert a string in an array

# Python program to split an array in two and store even numbers in one array and odd numbers in the other.

# Python program to perform insertion sort on an array.

# Python program to store the Unicode value of each character in the given array.


# def difference_from_average(arr):
#     if not arr:  # Edge case: empty list
#         return []
#     avg = sum(arr) / len(arr)  # O(n)    
#     # Return list of differences
#     return [num - avg for num in arr]
# # Example
# arr = [10, 20, 30, 40]
# print(difference_from_average(arr))


# # Convert string to list of characters
# def string_to_char_array(s):
#     return list(s)
# print(string_to_char_array("kiran"))

# # Convert space-separated string to array of words
# def string_to_word_array(s):
#     return s.split()
# print(string_to_word_array("I love Python"))

# # Convert comma-separated string to integer array
# def string_to_int_array(s):
#     return list(map(int, s.split(",")))
# print(string_to_int_array("1,2,3,4"))


# def split_even_odd(arr):
#     even = []
#     odd = []
#     for num in arr:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     return even, odd
# # Example
# arr = [1, 2, 3, 4, 5, 6]
# even, odd = split_even_odd(arr)
# print("Even:", even)
# print("Odd:", odd)


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         # Shift elements greater than key
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# # Example
# arr = [5, 2, 9, 1, 5, 6]
# print(insertion_sort(arr))
# def unicode_values(char_array):
#     return [ord(char) for char in char_array]
# # Example
# arr = ['A', 'b', 'C']
# print(unicode_values(arr))


# # If Input is String Instead of Array
# def unicode_from_string(s):
#     return [ord(ch) for ch in s]
# print(unicode_from_string("ABC"))


