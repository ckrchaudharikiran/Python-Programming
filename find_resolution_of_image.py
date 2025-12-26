from PIL import Image   # no need to import PIL separately

img = Image.open("C:/Users/A200386036/OneDrive - Deutsche Telekom AG/Desktop/Kiran- Coding/Python/Image.jpg")

width, height = img.size
print(width, "*", height)

