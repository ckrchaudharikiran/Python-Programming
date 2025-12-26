# year = int(input("Enter the Year: "))

# if year % 400 == 0:
#     print(f"{year} is a leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")



#shorter code
year = int(input("Enter the Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
