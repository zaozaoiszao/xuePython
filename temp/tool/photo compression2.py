from PIL import Image
from tqdm import tqdm
a=1
# 打开文件  
with open('图片.zp', 'r') as file:
    content = file.read()
    tokens = content.split(';')
    Width=int(tokens[0].split(',')[0],16)
    Height=int(tokens[0].split(',')[1],16)
img = Image.new('RGB', (Width, Height),'white') 

# 访问图片的像素数据  
pixels = img.load() 

for x in tqdm(range(Width)):  # 遍历宽度  
    for y in range(Height):  # 遍历高度 
        i=tokens[a]
        rgb = i.split(',')
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        pixels[x, y] = (int(r,16),int(g,16),int(b,16))
        a+=1
img.save('my_image.png')