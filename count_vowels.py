a = str(input("Enter the statement: "))
vowels = "aeiou"
a = a.casefold()

count = {}.fromkeys(vowels, 0)

for char in a:
    if char in count:
        count[char] += 1

print("Vowel counts:", count)



# a = input("Enter the statement: ").casefold()
# vowels = "aeiou"

# count = {key: sum(1 for ch in a if ch == key) for key in vowels}
# print(count)



# from collections import Counter

# a = input("Enter the statement: ").casefold()
# vowels = "aeiou"

# count = Counter(a)   # counts all characters
# vowel_counts = {v: count[v] for v in vowels}

# print("Vowel counts:", vowel_counts)
