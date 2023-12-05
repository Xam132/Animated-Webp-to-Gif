from PIL import Image
import os
count = 1
path = ''

def web_gif(item,count):
    im = Image.open(path+item)
    im.info.pop('background', None)
    im.save(path+str(count)+'.gif', 'gif', save_all=True)

dir_list = os.listdir(path)

for i in dir_list:
    print(count)
    web_gif(i,count)
    count += 1

