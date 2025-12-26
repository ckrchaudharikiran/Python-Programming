num = input("Enter a number: ")

def float_check(num):
    try:
        float(num)
        return True
    except:
        return False
print(float_check(num))

# Avoid bare except: (it catches everything, even unexpected errors). Instead, catch ValueError:
# def float_check(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False


# If you want to check only valid float numbers (not things like "nan" or "inf", which float() accepts), you can add an extra check:

# import math

# def float_check(num):
#     try:
#         val = float(num)
#         return math.isfinite(val)  # excludes nan and inf
#     except ValueError:
#         return False
