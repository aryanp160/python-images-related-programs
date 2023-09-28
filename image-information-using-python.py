#importing PIL.
from PIL import Image


#opening the image.
image = Image.open('sample-image.jpg')


#image.filename helps us to access the name of the file.
print("Filename: ", image.filename)


#image.format tells us the size as a width and height tuple(in pixels).
print("Size: ", image.size)


#you can also get image's height and width independetly using these two commands.
print("Width: ", image.width)
print("Height: ", image.height)


#image.format helps usto access the format of the file.
# Eg- JPG, PNG, GIF, HEIF etc..
print("Format: ", image.format)


#image.mode helps usto access the mode of the file.
# Eg- RGB, RFBA, CMYK, etc.
print("Mode: ", image.mode)

 
#closing the image.
image.close()
