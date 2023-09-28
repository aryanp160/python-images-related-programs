#importing PIL.
from PIL import Image
 
try:
    #opening the image.
    image = Image.open('wrong-filename.jpg')
 
    #converting image from .jpg to .png format.
    image.save("converted-png-image.png")
    print("Image successfully converted!")
 
except FileNotFoundError:
    print("Couldn't find the specified image")
