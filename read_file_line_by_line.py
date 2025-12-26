# using readlines()
f= open("C:/Users/A200386036/OneDrive - Deutsche Telekom AG/Desktop/Kiran- Coding/Python/file.txt","r")
lines = f.readlines()
print(lines)
new_lines = [x.strip() for x in lines]
print(new_lines)

#fixed code
# with open("C:/Users/A200386036/OneDrive - Deutsche Telekom AG/Desktop/Kiran- Coding/Python/file.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

#     new_lines = [x.strip() for x in lines]  # ✅ use strip()
#     print(new_lines)

#using for loop
# f= open("C:/Users/A200386036/OneDrive - Deutsche Telekom AG/Desktop/Kiran- Coding/Python/file.txt","r")
# line= [line for line in f]
# print(line)
# new_lines = [x.strip() for x in line]
# print(new_lines)
