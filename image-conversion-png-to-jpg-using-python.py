#importing PIL.
from PIL import Image
 
#opening the image.
image = Image.open('sample-png-image.png')
 
#specifying the RGB mode to the image.
image = image.convert('RGB')
 
#converting an image from .png to .jpg format.
image.save("converted-jpg-image.jpg")
print("Image successfully converted.")

