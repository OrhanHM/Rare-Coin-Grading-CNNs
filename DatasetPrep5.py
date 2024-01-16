import os
from os.path import exists
import pandas as pd


def pathToInfo(fp):
    isObv = False
    split = fp.split('g')
    split1 = split[3]
    split2 = split[4]
    if split1.count('o') == 1:
        imgInd = int(split1.split('o')[0])
        isObv = True
    else:
        imgInd = int(split1.split('r')[0])
    augInd = int(split2[4:-3])
    return isObv, imgInd, augInd


dataframe = pd.read_csv('FullyCutDataframe2.csv')
Dict = {
    'Grade': [],
    'Large Obverse Path': [],
    'Large Reverse Path': [],
    'Medium Obverse Path': [],
    'Medium Reverse Path': [],
    'Small Obverse Path': [],
    'Small Reverse Path': []
}


largeImgPath = '/Volumes/Toshiba/ImageAugment1000x1000'
medImgPath = '/Volumes/Toshiba/ImageAugment512x512'
smallImgPath = '/Volumes/Toshiba/ImageAugment256x256'
modelFp = '/Volumes/Toshiba/ImageAugment1000x1000/img0rev_augment0.jpg'


filenames = os.listdir(largeImgPath)
imagenames = [name for name in filenames if name.endswith('.jpg')]
print('Got filenames')
dataPoints = []
for name in imagenames:
    path = largeImgPath + '/' + name
    info = pathToInfo(path)
    grade = dataframe.at[info[1], 'Grade']
    if info[0]:
        dataPoints.append((info[1], info[2], grade, name))
# inds format = (image index, augment index, grade, filename)
print('got data points')
print(len(dataPoints))

dflen = 0
for ind, dataPoint in enumerate(dataPoints):
    if ind % 1000 == 0:
        print(ind)
    coinGrade = dataPoint[2]
    obvPath = dataPoint[3]
    revPath = obvPath.replace('obv', 'rev')
    largeObvPath = largeImgPath + '/' + obvPath
    largeRevPath = largeImgPath + '/' + revPath
    medObvPath = medImgPath + '/' + obvPath
    medRevPath = medImgPath + '/' + revPath
    smallObvPath = smallImgPath + '/' + obvPath
    smallRevPath = smallImgPath + '/' + revPath
    Dict['Grade'].append(coinGrade)
    Dict['Large Obverse Path'].append(largeObvPath)
    Dict['Large Reverse Path'].append(largeRevPath)
    Dict['Medium Obverse Path'].append(medObvPath)
    Dict['Medium Reverse Path'].append(medRevPath)
    Dict['Small Obverse Path'].append(smallObvPath)
    Dict['Small Reverse Path'].append(smallRevPath)

    '''newDF.loc[dflen] = [coinGrade, largeObvPath, largeRevPath, medObvPath, medRevPath, smallObvPath, smallRevPath]
    dflen += 1'''

newDF = pd.DataFrame(Dict)
newDF.to_csv('FinishedDataset.csv', index=False)
