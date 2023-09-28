In these programs, we'll extract information of image and converting it into any other form using python's library "PILLOW".

According to the official pillow documentation, the mode of an image is a string that defines the type and depth of a pixel in the image. The pillow library supports 11 modes including the following standard modes:

~RGB (3x8-bit pixels, true color).
~RGBA (4x8-bit pixels, true color with transparency mask).
~CMYK (4x8-bit pixels, color separation).
~HSV (3x8-bit pixels, Hue, Saturation, Value color space).


Converting an image to PNG preserves any transparency while, You’ll lose any transparency in an image if you convert it to JPG format. For example, if you convert a transparent GIF image to a PNG image, the result will still be a transparent image.
If you try to preserve the transparency using the RGBA mode, Python will throw an error.

