import pandas as pd
import os
from os.path import exists


# Remove 60 class bc there were only 90 data points
dataframe = pd.read_csv('Cut64to67.csv')

bases = list(dataframe['Base Path'])
grades = list(dataframe['Grade'])
print(grades.count(60))

dropList = []
for ind, val in enumerate(grades):
    if val == 60:
        dropList.append(ind)
        '''delpath = bases[ind] + 'obv.jpg'
        if exists(delpath):
            os.remove(delpath)
            delpath = bases[ind] + 'rev.jpg'
            os.remove(delpath)'''

dataframe = dataframe.drop(labels=dropList, axis=0)
dataframe.to_csv('FullyCutDataframe.csv', index=False)
