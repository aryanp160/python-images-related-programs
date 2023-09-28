#importing PIL.
from PIL import Image
 
#opening the image.
image = Image.open('sample-jpg-image.jpg')
 
#converting image from .jpg to .png format.
image.save("converted-png-image.png")
print("Image successfully converted!")



