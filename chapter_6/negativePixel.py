from image import *
def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newBlue = 255 - oldPixel.getBlue()
    newGreen = 255 - oldPixel.getGreen()
    newPixel = Pixel(newRed,newGreen,newBlue)
    return newPixel

def makeNegative(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.get_width()
    height = oldImage.get_height()

    myImageWindow = ImageWin(width * 2,height,'Negative Image')
    oldImage.draw(myImageWindow)

    newIm = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col,row)
            newPixel = negativePixel(oldPixel)
            newIm.setPixel(col,row,newPixel)

    newIm.setPosition(width + 1,0)
    newIm.draw(myImageWindow)
    newIm.save('1_negative.png','png')
    myImageWindow.exit_on_click()


if __name__ == "__main__":
    def main():
        makeNegative('1.png')

    main()

    