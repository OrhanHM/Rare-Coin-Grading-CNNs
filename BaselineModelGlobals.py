import numpy as np
import pandas as pd
import sklearn
import os
from sklearn.model_selection import train_test_split


def divideDataToBatches(xSize, ySize):
    global trainLen
    global testLen
    global trainNamePortions
    global trainGradePortions
    global testNamePortions
    global testGradePortions

    trainNamePortions = []
    trainGradePortions = []
    for i in range(0, trainLen, xSize):
        if i + xSize < trainLen:
            trainNamePortions.append(trainNames[i:i + xSize])
            trainGradePortions.append(trainGrades[i:i + xSize])
        else:
            trainNamePortions.append(trainNames[i:])
            trainGradePortions.append(trainGrades[i:])

    testNamePortions = []
    testGradePortions = []
    for i in range(0, testLen, ySize):
        if i + ySize < testLen:
            testNamePortions.append(testNames[i:i + ySize])
            testGradePortions.append(testGrades[i:i + ySize])
        else:
            testNamePortions.append(testNames[i:])
            testGradePortions.append(testGrades[i:])


imgPath = '/Volumes/Toshiba/ImageAugment256x256'
'''filenames = os.listdir(imgPath)
imagenames = [name for name in filenames if name.endswith('.jpg')]
totalImages = len(imagenames)'''
dataframe = pd.read_csv('NewFinalDataframe.csv')[['Grade', 'Large Obverse Path', 'Large Reverse Path']]
X = [(dataframe.at[i, 'Large Obverse Path'], dataframe.at[i, 'Large Reverse Path']) for i in range(len(dataframe))]
y = [dataframe.at[i, 'Grade'] for i in range(len(dataframe))]
uniqueGrades = np.unique(np.asarray(dataframe['Grade']))  # 29 unique grades

trainNames, testNames, trainGrades, testGrades = train_test_split(X, y, random_state=1, test_size=0.25)
trainLen = len(trainGrades)
testLen = len(testGrades)
trainNamePortions = []
trainGradePortions = []
testNamePortions = []
testGradePortions = []
