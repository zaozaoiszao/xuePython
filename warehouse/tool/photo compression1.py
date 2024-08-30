from PIL import Image
from tqdm import tqdm
a=0
path=input('/>')
#C:\Users\Administrator\Pictures\0.png
img = Image.open(r'%s' %path)
img = img.convert("RGB")
width, height = img.size  
print(f"Width: {width}, Height: {height}")

with open('图片.zp', 'w', encoding='utf-8') as file:  
    file.write(f"{hex(width)},{hex(height)}")
    for x in tqdm(range(width)):
        for y in range(height):
            r, g, b = img.getpixel((x, y))  
            file.write(f";{hex(r)},{hex(g)},{hex(b)}")
            a+=1
print(f'共{a}个像素点')