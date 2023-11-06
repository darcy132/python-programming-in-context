import glob
import threading
import os
from image import *

def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newBlue = 255 - oldPixel.getBlue()
    newGreen = 255 - oldPixel.getGreen()
    newPixel = Pixel(newRed,newGreen,newBlue)
    return newPixel


def negative_image(png_file):

    image = FileImage(png_file)


    
    width = image.get_width()
    height = image.get_height()

   
    newIm = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            oldPixel = image.getPixel(col,row)
            newPixel = negativePixel(oldPixel)
            newIm.setPixel(col,row,newPixel)

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
    large_folder = "/home/brown/Pictures/women_neg"

    # Create the large folder if it doesn't exist.
    if not os.path.exists(large_folder):
        os.makedirs(large_folder)

    # Call the multi_thread_negative_images() function.
    multi_thread_negative_images(png_folder, large_folder)
