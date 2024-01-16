from os import listdir
from PIL import Image
from os.path import exists
from time import time


oldPath = '/Volumes/Toshiba/ImageAugment1000x1000/'
newPath1 = '/Volumes/Toshiba/ImageAugment512x512/'
newPath2 = '/Volumes/Toshiba/ImageAugment256x256/'

filenames = listdir(oldPath)

start = time()
for ind, name in enumerate(filenames):
    if ind % 1000 == 0:
        end = time()
        print(ind, end-start)
    path = oldPath+name
    if exists(path) and 'img' in path:
        im = Image.open(oldPath+name).resize((512, 512))
        im.save(newPath1+name)
        im = im.resize((256, 256))
        im.save(newPath2+name)
