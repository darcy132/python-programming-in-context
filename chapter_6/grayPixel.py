from image import *
def grayPixel(oldPixel):
    intensitySum = oldPixel.getRed() + oldPixel.getGreen()\
                    + oldPixel.getBlue()
    aveRGB = intensitySum // 3
    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel

def makeGrayScale(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.get_width()
    height = oldImage.get_height()

    myImageWindow = ImageWin(width * 2,height,'GrayScale')
    oldImage.draw(myImageWindow)  
    newIm = EmptyImage(width,height)
    
    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col,row)
            newPixel = grayPixel(oldPixel)
            newIm.setPixel(col,row,newPixel)

    newIm.setPosition(width + 1,0)
    newIm.draw(myImageWindow)
    newIm.save('butterfly_gray.png','png')
    myImageWindow.exit_on_click()




if __name__ == "__main__":
    def main():
        makeGrayScale('free-butterfly-1.png')


    main()