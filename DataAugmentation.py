import pandas as pd
from PIL import Image
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import matplotlib.pyplot as plt
from os.path import exists
from time import time
import random

dataframe = pd.read_csv('FullyCutDataframe2.csv')

ia.seed(1)
augmenter = iaa.Sequential([
    iaa.CropAndPad(percent=(.35, .27), pad_cval=255),
    iaa.pillike.Affine(
        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
        rotate=(-15, 15),
        shear=(-1, 1),
        fillcolor=255
    )
])


start = time()
classes = list(np.unique(np.asarray(dataframe['Grade'])))
count = [list(dataframe['Grade']).count(grade) for grade in classes]
reps = [round(8000/list(dataframe['Grade']).count(grade)) for grade in classes]
splitUpClasses = [[] for i in classes]

for ind, val in enumerate(list(dataframe['Grade'])):
    gradeInd = classes.index(val)
    splitUpClasses[gradeInd].append(ind)

for repInd, indList in enumerate(splitUpClasses):
    print(classes[repInd])
    for imgInd in indList:
        obvpath = dataframe.at[imgInd, 'Obverse Path']
        im = Image.open(obvpath)
        obvPix = np.reshape(np.asarray(im, dtype=np.uint8), (1, 1000, 1000, 3))
        revpath = dataframe.at[imgInd, 'Reverse Path']
        im = Image.open(revpath)
        revPix = np.reshape(np.asarray(im, dtype=np.uint8), (1, 1000, 1000, 3))
        for rep in range(reps[repInd]):
            newObvPath = '/Volumes/Toshiba/ImageAugment1000x1000/img'+str(imgInd)+'obv_augment'+str(rep)+'.jpg'
            newRevPath = '/Volumes/Toshiba/ImageAugment1000x1000/img'+str(imgInd)+'rev_augment'+str(rep)+'.jpg'
            obvAugmented = augmenter(images=obvPix)
            im = Image.fromarray(obvAugmented[0])
            im.save(newObvPath)
            revAugmented = augmenter(images=revPix)
            im = Image.fromarray(revAugmented[0])
            im.save(newRevPath)

