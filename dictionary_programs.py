from collections import defaultdict
# Using int as the default factory to initialize missing keys with 0
d = defaultdict(int)
# Incrementing the value for key 'a'
d["a"] += 1  
print(d)  

# Using list as the default factory to initialize missing keys with an empty list
d = defaultdict(list)
# Appending to the list for key 'b'
d["b"].append(1)  
print(d)  

# Using a custom function as the default factory
def default_value():
    return "N/A"

d = defaultdict(default_value)
print(d["c"]) 


# # Creating a dictionary
# student_info = {
#     "name": "Alice",
#     "age": 21,
#     "major": "Computer Science"
# }

# # Removing items based on conditions
# keys_to_remove = ["age", "major"]
# for key in keys_to_remove:
#     student_info.pop(key, None)

# print(student_info)  


# student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# # Looping through values 
# for value in student.values():
#    print(value)

# student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# # Looping through keys 
# for key in student.keys():
#    print(key)

# student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# # Looping through key-value pairs 
# for key, value in student.items():
#    print(key, value)

# student = {"name": "Alice", "age": 21, "major": "Computer Science"}
# for key, value in student.items():
#    print(key, value)

# student = {"name": "Alice", "age": 21, "major": "Computer Science"}
# for key in student:
#    print(key, student[key])


# import copy

# original_dict = {
#     "name": "Alice",
#     "age": 25,
#     "skills": ["Python", "Data Science"],
#     "education": {
#       "degree": "Bachelor's",
#       "field": "Computer Science"
#    }
# }

# # Creating a deep copy
# deep_copy = copy.deepcopy(original_dict)

# # Modifying the deep copy
# deep_copy["age"] = 26
# deep_copy["skills"].append("Machine Learning")
# deep_copy["education"]["degree"] = "Master's"

# # Retrieving both dictionaries
# print("Original dictionary:", original_dict)
# print("Deep copy:", deep_copy)


# original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
# shallow_copy = dict(original_dict)

# # Modifying the shallow copy
# shallow_copy["age"] = 31
# shallow_copy["skills"].append("C#")

# print("Original dictionary:", original_dict)
# print("Shallow copy:", shallow_copy)



# original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
# shallow_copy = original_dict.copy()

# # Modifying the shallow copy
# shallow_copy["age"] = 26
# shallow_copy["skills"].append("Machine Learning")

# print("Original dictionary:", original_dict)
# print("Shallow copy:", shallow_copy)


