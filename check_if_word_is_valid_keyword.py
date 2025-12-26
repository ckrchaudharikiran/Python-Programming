import keyword
words = ["break","stop","Kiran","tsystems"]
for i in range(len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],"is a keyword in python")
    else:
        print(words[i], "is not a keyword in python")



# cleaner version
import keyword

words = ["break", "stop", "Kiran", "tsystems"]

for word in words:
    if keyword.iskeyword(word):
        print(f"{word} is a keyword in python")
    else:
        print(f"{word} is not a keyword in python")
