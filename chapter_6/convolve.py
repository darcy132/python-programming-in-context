import math
from grayPixel import *
from pixelMapper import *
from image import *


def convolve(anImage,pixelRow,pixelCol,kernel):
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1

    sum = 0
    for row in range(kernelRowBase,kernelRowBase+3):
        for col in range(kernelColumnBase,kernelColumnBase+3):
            kColIndex = col - kernelColumnBase
            kRowIndex = row - kernelRowBase

            aPixel = anImage.getPixel(col,row)
            intensity = aPixel.getRed()

            sum = sum + intensity*kernel[kRowIndex][kColIndex]
    return sum

def edgeDetect(theImage):
    grayImage = pixelMapper(theImage,grayPixel)
    newIm = EmptyImage(grayImage.getWidth(),grayImage.getHeight())
    black = Pixel(0,0,0)
    white = Pixel(255,255,255)
    XMask = [[-1,-2,-1],[0,0,0],[1,2,1]]
    YMask = [[-1,-2,-1],[0,0,0],[1,2,1]]

    for row in range(1,grayImage.get_height()-1):
        for col in range(1,grayImage.get_width()-1):
            gX = convolve(grayImage,row,col,XMask)
            gY = convolve(grayImage,row,col,YMask)
            g = math.sqrt(gX**2+gY**2)

            if g > 175:
                newIm.set_pixel(col,row,black)
            else:
                newIm.set_pixel(col,row,white)
    
    return newIm

def makeEdge(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.get_width()
    height = oldImage.get_height()

    myImageWindow = ImageWin(width * 2,height,'edgeDetect Image')
    oldImage.draw(myImageWindow)

    newIm = edgeDetect(oldImage)

    newIm.setPosition(width + 1,0)
    newIm.draw(myImageWindow)
    newIm.save('butterfly_edge.png','png')
    myImageWindow.exit_on_click()

def main():
    makeEdge('free-butterfly-1.png')

if __name__ == "__main__":
    main()