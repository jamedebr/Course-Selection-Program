import os,sys
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageChops
im1= Image.open("peepoHappy.png")
im2 = Image.open("POG_MLG-removebg-preview.png")
xsize, ysize = im1.size
im2 = im2.resize(im1.size)



print("what edit u want? crop, saturate, or flip?")
editType = input()
editType = editType.upper()


if editType == "CROP":

    print("Where do you want to crop from, top left, lop right, bottom left, bottom right, or middle?")
    cropType = input()
    cropType = cropType.upper()
    if cropType == "TOP LEFT":
        print("how wide (in pixels)? Max size = "+ str(xsize))
        cropWidth = input()
        print("how tall (in pixels)? Max size = "+ str(ysize))
        cropHeight = input()
        box = (0, 0, int(cropWidth), int(cropHeight))
        image = im1.crop(box)
        image.show()

    if cropType == "TOP RIGHT":
        print("how wide (in pixels)? Max size = " + str(xsize))
        cropWidth = input()
        print("how tall (in pixels)? Max size = " + str(ysize))
        cropHeight = input()
        box = (int(xsize) - int(cropWidth), 0, xsize, cropHeight)
        image = im1.crop(box)
        image.show()

    if cropType == "BOTTOM LEFT":
        print("how wide (in pixels)? Max size = " + str(xsize))
        cropWidth = input()
        print("how tall (in pixels)? Max size = " + str(ysize))
        cropHeight = input()
        box = (0, int(ysize) - int(cropHeight), cropWidth, ysize)
        image = im1.crop(box)
        image.show()

    if cropType == "BOTTOM RIGHT":
        print("how wide (in pixels)? Max size = " + str(xsize))
        cropWidth = input()
        print("how tall (in pixels)? Max size = " + str(ysize))
        cropHeight = input()
        box = (int(xsize) - int(cropWidth), int(ysize) - int(cropHeight), xsize, ysize)
        image = im1.crop(box)
        image.show()

    if cropType == "MIDDLE":
        print("how wide (in pixels)? Max size = " + str(xsize))
        cropWidth = input()
        print("how tall (in pixels)? Max size = " + str(ysize))
        cropHeight = input()
        box = (int(xsize)/2 - int(cropWidth)/2, int(ysize)/2 - int(cropHeight)/2, int(xsize)/2 + int(cropWidth)/2, int(ysize)/2 + int(cropHeight)/2)
        image = im1.crop(box)
        image.show()

if editType == "ASCEND":

    image = im1.point(lambda i: i * 20)
    image.show()
if editType == "SATURATE":
    print("how much would you like to satuate it? Recommended range 2-20")
    saturationValue = input()
    image = ImageEnhance.Contrast(im1)
    image.enhance(int(saturationValue)).show()

if editType == "FLIP":

    image = im1.transpose(Image.Transpose.ROTATE_180)
    image.show()

if editType == "MLG":
    image = ImageChops.overlay(im1, im2)
    image = ImageEnhance.Contrast(image)
    image.enhance(2).show()
    #image.show()



#while RunProgram == True:
#    if askPhoto == True:
#        print('Welcome to your photo editor!')
#        print('please select which photo to edit')
#        print('a,','#somehow your photo here')
#        print('b,', '#somehow your photo here')
#        print('c,', '#somehow your photo here')
#        askPhoto = False
#        PhotoDetermine = input()
#        if PhotoDetermine == 'a':
#            print('Great choice!')
#    if TypeEdit == True:
#        print('what type of edit do you want to make?')
#        print('Options: Rotate, Crop, Brighten, Dim, Change file type')
#        TypeEdit = False
