import string

punc = string.punctuation
print("Punctuation characters:", punc)

text = input("Enter String: ")
empty_str = ""
for i in text:
    if i not in punc:
        empty_str += i
print("String without punctuation:", empty_str)

