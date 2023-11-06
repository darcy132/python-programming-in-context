import glob
import threading
import os
from image import *
import math
from grayPixel import *
from pixelMapper import *



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



def negative_image(png_file):

    image = FileImage(png_file)

   
    newIm = edgeDetect(image)

    # Save the negative image to a new file
    negative_image_file = os.path.join(large_folder, os.path.basename(png_file))
    newIm.save(negative_image_file)

def multi_thread_negative_images(png_folder, large_folder):

    threads = []

    # Iterate over the PNG files in the folder and create a new thread for each file.
    for png_file in glob.glob(os.path.join(png_folder, "*.png")):
        thread = threading.Thread(target=negative_image, args=(png_file,))
        threads.append(thread)

    # Start all of the threads.
    for thread in threads:
        thread.start()

    # Wait for all of the threads to finish.
    for thread in threads:
        thread.join()

if __name__ == "__main__":

    # Get the path to the PNG folder and the large folder.
    png_folder = "/home/brown/Pictures/women"
    large_folder = "/home/brown/Pictures/women_edge"

    # Create the large folder if it doesn't exist.
    if not os.path.exists(large_folder):
        os.makedirs(large_folder)
    multi_thread_negative_images(png_folder, large_folder)