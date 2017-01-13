# TransparencyTools

A few weeks ago, I was working on a game and I wanted to add transparent text. I looked around and there simply were no easy ways to do this. There were Photoshop tutorials but I didn't want to pay for it and even with PS, there were just too many steps. So, of course, I wrote these short scripts to do the job. Feel free to use and edit as you will.

**tblack.py**
This file will remove text from an image with a white background. My first method to remove black text from a white image was trying to remove all black pixels. That was horribly unsuccessful. There was a ton of noise in the edges. So, I used the reverse method which converts any non-white pixel to a transparent pixel.

**twhite.py**
This file will do the same thing as the tblack.py except it will remove text from an image with a black background. If your image has a solid colored background that is not black or white, you can just change the RGB values in line 10 and run this file. If, however, you have a background that is not a solid color, try messing with the third file, background.py.

**background.py**
The primary purpose of this file is to remove the white background from an image. There are two important parameters to remember here - minpix and graymax. Minpix is the minimum pixel values in order for a pixel to be removed and graymax sets how close the pixel values have to be. This thresholding makes the final image smooth. If your resulting image does not remove enough, consider decreasing minpix or increasing graymax. Of course, it it removes too much, try increasing minpix and decreasing graymax.

Now, if you wish to remove white text from a non-white background, you can use this file as well.

**Command Line Input:**
python file_name image_name

For example, running "python tblack.py text.png" will save an image called 2text.png.
