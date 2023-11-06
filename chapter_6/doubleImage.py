from image import *
def doubleImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW*2,oldH*2)

    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col,row)

            newIm.setPixel(2*col,2*row,oldPixel)
            newIm.setPixel(2*col +1,2*row,oldPixel)
            newIm.setPixel(2*col,2*row+1,oldPixel)
            newIm.setPixel(2*col + 1,2*row +1,oldPixel)
    
    return newIm

def makeDoubleImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.get_width()
    height = oldImage.get_height()

    myImageWindow = ImageWin(width * 2,height*3,'DoubleImage')
    oldImage.draw(myImageWindow)  
 
    
    newIm = doubleImage(oldImage)
    newIm.setPosition(0,oldImage.getHeight()+1)
    newIm.draw(myImageWindow)
    newIm.save('butterfly_double.png','png')
    myImageWindow.exit_on_click()




if __name__ == "__main__":
    def main():
        makeDoubleImage('free-butterfly-1.png')


    main()