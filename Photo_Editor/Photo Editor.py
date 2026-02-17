


#just replaced selected Image with Image, now Image.crop doesn't exist lol




import os,sys
from PIL import ImageEnhance, Image, ImageChops, ImageDraw, ImageEnhance

im1 = Image.open("peepoHappy.png")
im2 = Image.open("POG_MLG-removebg-preview.png")
im3 = Image.open("peeposad.png")
im4 = Image.open("peepocheer.jpg")

im4 = im4.save("peepocheer.png")

xsize, ysize = im1.size
im2 = im2.resize(im1.size)

print("Which Peepo do you want? Happy, Sad, or Cheer?")
selection = input()
selection = selection.upper()
print(selection+" selected")

Image = im1
if selection == "HAPPY":
    Image = im1
if selection == "SAD":
    Image = im3
if selection == "CHEER":
    Image = im4


editAgain = 1


while editAgain == 1:

    print("what edit u want? crop, saturate, or rotate?")
    editType = input()
    editType = editType.upper()

    if editType == "CROP":

        print("Where do you want to crop from, top left, top right, bottom left, bottom right, or middle?")
        cropType = input()
        cropType = cropType.upper()
        if cropType == "TOP LEFT":
            print("how wide (in pixels)? Max size = "+ str(xsize))
            cropWidth = input()
            print("how tall (in pixels)? Max size = "+ str(ysize))
            cropHeight = input()
            box = (0, 0, int(cropWidth), int(cropHeight))
            Image = Image.crop(box)
            Image.show()

        if cropType == "TOP RIGHT":
            print("how wide (in pixels)? Max size = " + str(xsize))
            cropWidth = input()
            print("how tall (in pixels)? Max size = " + str(ysize))
            cropHeight = input()
            box = (int(xsize) - int(cropWidth), 0, xsize, int(cropHeight))
            Image = Image.crop(box)
            Image.show()

        if cropType == "BOTTOM LEFT":
            print("how wide (in pixels)? Max size = " + str(xsize))
            cropWidth = input()
            print("how tall (in pixels)? Max size = " + str(ysize))
            cropHeight = input()
            box = (0, int(ysize) - int(cropHeight), cropWidth, ysize)
            Image = Image.crop(box)
            Image.show()

        if cropType == "BOTTOM RIGHT":
            print("how wide (in pixels)? Max size = " + str(xsize))
            cropWidth = input()
            print("how tall (in pixels)? Max size = " + str(ysize))
            cropHeight = input()
            box = (int(xsize) - int(cropWidth), int(ysize) - int(cropHeight), xsize, ysize)
            Image = Image.crop(box)
            Image.show()

        if cropType == "MIDDLE":
            print("how wide (in pixels)? Max size = " + str(xsize))
            cropWidth = input()
            print("how tall (in pixels)? Max size = " + str(ysize))
            cropHeight = input()
            box = (int(xsize)/2 - int(cropWidth)/2, int(ysize)/2 - int(cropHeight)/2, int(xsize)/2 + int(cropWidth)/2, int(ysize)/2 + int(cropHeight)/2)
            Image = Image.crop(box)
            Image.show()

    if editType == "ASCEND":
        Image = Image.point(lambda i: i * 20)
        Image.show()

    if editType == "SATURATE":
        print("how much would you like to saturate it? Recommended range 2-30")
        saturationValue = input()
        Image = ImageEnhance.Contrast(Image)
        Image = Image.enhance(int(saturationValue))
        Image.show()



    if editType == "ROTATE":
        print("How much do you want to rotate by?")
        rotateAngle = input()
        Image = Image.rotate(angle=float(rotateAngle))
        Image.show()

    if editType == "MLG":
        Image = ImageChops.overlay(Image, im2)
        Image = ImageEnhance.Contrast(Image)
        Image.enhance(2)
        Image.show()

    print("would you like to make another edit? (Y/N)")
    moreEdit = input()
    moreEdit = moreEdit.upper()
    if moreEdit == "Y":
        editAgain = 1
    if moreEdit == "N":
        editAgain = 0

    # Image.save("editedImage.png")
    # Image.close()
    # Image = Image.open("editedImage.png")

print("finished editing")
Image.show()