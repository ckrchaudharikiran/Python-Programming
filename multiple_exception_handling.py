text = str(input("Enter text here: "))
try:
    num = int(input("Enter the number here: "))
    print(text+num)
except(ValueError, TypeError) as e:
    print(e)