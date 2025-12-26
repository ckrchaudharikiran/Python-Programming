# word = input("Enter the word: ")
# reverse = word[::-1]
# if word == reverse:
#     print("Its is a Palindrome")
# else:
#     print("It is not a Palindrome")


#Improved Version of code
word = input("Enter the word: ")

# normalize: lowercase + remove spaces
normalized = word.replace(" ", "").lower()
reverse = normalized[::-1]

if normalized == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
