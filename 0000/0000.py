#-*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

#msgNum从1到99取一个随机数
msgNum = str(random.randint(1,99))

#Read image
im = Image.open("kxrr.png")
w,h = im.size
wDraw = 0.8 * w
hDraw = 0.08 * w

#Draw image
font = ImageFont.truetype("C:\Windows\Fonts\Inkfree.ttf", 30)# use absolute font path to fix 'IOError: cannot open resource'
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), msgNum, font=font, fill=(255, 33, 33))

#Save image
im.save('kxrr_msg.png','png')
