import os, sys
from PIL import Image
from PIL import ImageEnhance
im = Image.open("peepoHappy.jpg")
print(im.format, im.size, im.mode)
xsize, ysize = im.size
r, g, b = im.split()
#box = (xsize/2, 0, xsize, ysize/2)
#im = im.crop(box)

#im = ImageEnhance.Color(im)
#im.enhance(50.0).show()

#im = ImageEnhance.Contrast(im)
#im.enhance(1.5).show()


#im.show()


if input() == "crop":
    boxIn = input()
    boxIn.split(",")
