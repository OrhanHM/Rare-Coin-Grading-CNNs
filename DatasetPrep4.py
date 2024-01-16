import pandas as pd
import os
from os.path import exists
import random


# trim down classes 64 through 67 to about 8000, but randomize this a bit
dataframe = pd.read_csv('PathDataSet.csv')

bases = list(dataframe['Base Path'])
grades = list(dataframe['Grade'])
print('Total images in folder:', len(grades) * 2)

final64 = random.randint(7750, 8250)
remove64 = grades.count(64) - final64
final65 = random.randint(7750, 8250)
remove65 = grades.count(65) - final65
final66 = random.randint(7750, 8250)
remove66 = grades.count(66) - final66
final67 = random.randint(7750, 8250)
remove67 = grades.count(67) - final67
totalDeleted = remove64 + remove65 + remove66 + remove67
inds64 = []
inds65 = []
inds66 = []
inds67 = []

for ind, val in enumerate(grades):
    if val == 64:
        inds64.append(ind)
    if val == 65:
        inds65.append(ind)
    if val == 66:
        inds66.append(ind)
    if val == 67:
        inds67.append(ind)

drop64 = random.sample(inds64, remove64)
drop65 = random.sample(inds65, remove65)
drop66 = random.sample(inds66, remove66)
drop67 = random.sample(inds67, remove67)
deleteInds = (drop64 + drop65 + drop66 + drop67)
deleteInds.sort()

for ind in deleteInds:
    delpath = bases[ind] + 'obv.jpg'
    if exists(delpath):
        os.remove(delpath)
        delpath = bases[ind] + 'rev.jpg'
        os.remove(delpath)

dataframe = dataframe.drop(labels=drop64, axis=0)
dataframe = dataframe.drop(labels=drop65, axis=0)
dataframe = dataframe.drop(labels=drop66, axis=0)
dataframe = dataframe.drop(labels=drop67, axis=0)

dataframe.to_csv('Cut64to67.csv')
print('Expected images in folder:', (len(grades)-totalDeleted)*2)
