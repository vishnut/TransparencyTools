from PIL import Image
import sys

img = Image.open(sys.argv[1])
img = img.convert("RGBA")
rgba = img.getdata()

tImage = []
for pixel in rgba:
  if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
    newpixel = (pixel[0],pixel[1],pixel[2])
  else:
    newpixel = (pixel[0],pixel[1],pixel[2],0)
  tImage.append(newpixel)
img.putdata(tImage)
img.save("2"+sys.argv[1], "PNG")
