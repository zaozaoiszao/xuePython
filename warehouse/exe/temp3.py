from PIL import Image
from tqdm import tqdm
a=0
pic=[]
path=input('/>')
#C:\Users\Administrator\Pictures\0.png
img = Image.open(r'%s' %path)
img = img.convert("RGB")
Width, Height = img.size  

for x in tqdm(range(Width)):
    for y in range(Height):
        r, g, b = img.getpixel((x, y))  
        pic.append(f"{r},{g},{b}")
        a+=1
print(f'共{a}个像素点')

a=0
img = Image.new('RGB', (Width, Height),'white')
pixels = img.load()
for x in tqdm(range(Width)):  # 遍历宽度  
    for y in range(Height):  # 遍历高度 
        i=pic[a]
        rgb = i.split(',')
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        pixels[x, y] = (int(r),int(g),int(b))
        a+=1
img.save('my_image.png')