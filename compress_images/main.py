from PIL import Image # pip install Pillow
from os import chdir
from glob import glob

path = './' # relative path to directory containing photos
image_format = 'jpg' # image file extension
quality = 20 # the lower the value, the worse quality and smaller is the compressed image 

chdir(path)
for filename in glob('./**.%s' % image_format):
    img = Image.open(filename)
    img.save('%s_compressed.jpg' % filename.replace(
        '.jpg', ''), optimize=True, quality=quality)
