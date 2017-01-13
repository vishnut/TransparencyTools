from PIL import Image
import sys
import numpy as np

img = Image.open(sys.argv[1])
img = img.convert("RGBA")
rgba = img.getdata()
minpix = 250
graymax = 10

tImage = []
for pixel in rgba:
  if pixel[0] > minpix and pixel[1] > minpix and pixel[2] > minpix and np.abs(pixel[0]-pixel[1]) < graymax and np.abs(pixel[1]-pixel[2]) < graymax and np.abs(pixel[2]-pixel[0]) < graymax:
    newpixel = (pixel[0],pixel[1],pixel[2], 0)
  else:
    newpixel = (pixel[0],pixel[1],pixel[2])
  tImage.append(newpixel)
img.putdata(tImage)
img.save("2"+sys.argv[1], "PNG")
