from PIL import Image # pip install Pillow
from os import chdir
from glob import glob

path = './' # relative path to directory containing photos
image_format = 'jpg' # image file extension
suffix = '_resized' # a filename suffix for scaled image files 

# Set either the width or height to which images in folder should be scaled
target_width = 300
target_height = None

chdir(path)
if target_width is not None:
    for filename in glob('./**.%s' % image_format):
        img = Image.open(filename)
        width_ratio = (target_width / float(img.size[0]))
        height = int(float(img.size[1]) * float(width_ratio))
        print(f'Scaling {filename} from {img.size} to [{target_width}, {height}]')
        img = img.resize((target_width, height))
        img.save(filename.replace(f'.{image_format}', f'{suffix}.{image_format}'))
elif target_height is not None:
    for filename in glob('./**.%s' % image_format):
        img = Image.open(filename)
        height_ratio = (target_height / float(img.size[1]))
        width = int(float(img.size[0]) * float(height_ratio))
        print(f'Scaling {filename} from {img.size} to [{width}, {target_height}]')
        img = img.resize((width, target_height))
        img.save(filename.replace(f'.{image_format}', f'{suffix}.{image_format}'))
else:
    print('No images were scaled')