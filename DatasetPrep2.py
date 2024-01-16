from PIL import Image
import numpy as np
from time import time
from os.path import exists

start = time()
for i in range(91821):
    if i % 1000 == 0:
        print(i)
    filename = '/Volumes/Toshiba/RawImages/img'+str(i+1)+'.jpg'
    newFp = '/Volumes/Toshiba/RawImagesSquare/img'+str(i+1)
    if exists(filename):
        im = Image.open(filename).resize((2000, 1000))
        im1 = im.crop((0, 0, 1000, 1000))
        im2 = im.crop((1000, 0, 2000, 1000))
        im1.save(newFp+'obv.jpg')
        im2.save(newFp+'rev.jpg')
end = time()
print(end-start)
