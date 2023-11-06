from image import *
def verticalFlip(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW,oldH)

    maxP = oldW -1
    for row in range(oldH):
        for col in range(oldW):

            oldPixel = oldImage.getPixel(maxP - col,row)

            newIm.setPixel(col,row,oldPixel)
    
    return newIm

def makeVerticalFlip(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.get_width()
    height = oldImage.get_height()

    myImageWindow = ImageWin(width * 2,height,'verticalFlip Image')
    oldImage.draw(myImageWindow)

    newIm = EmptyImage(width,height)
    newIm = verticalFlip(oldImage)

    newIm.setPosition(width + 1,0)
    newIm.draw(myImageWindow)
    newIm.save('butterfly_vert.png','png')
    myImageWindow.exit_on_click()


if __name__ == "__main__":
    def main():
        makeVerticalFlip('free-butterfly-1.png')

    main()

    