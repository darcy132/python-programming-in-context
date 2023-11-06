from image import *
def pixelMapper(fileImage,rgbFunction):


    width = fileImage.getWidth()
    height = fileImage.getHeight()
    newIm = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            oldPixel = fileImage.getPixel(col,row)
            newPixel = rgbFunction(oldPixel)
            newIm.setPixel(col,row,newPixel)

    return newIm

