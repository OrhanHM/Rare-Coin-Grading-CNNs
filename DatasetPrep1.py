from os.path import isfile
import pandas as pd

dataframe = pd.read_csv('realDataSet.csv')
dataframe['Filepath'] = ['' for i in range(len(dataframe['Grade']))]

generalPath = '/Volumes/Toshiba/RawImages/'
deleteList = []
counter = 0
for ind, val in enumerate(dataframe['Grade']):
    imgName = 'img' + str(ind + 1) + '.jpg'
    imgPath = generalPath + imgName
    if isfile(imgPath):
        dataframe.loc[ind, 'Filepath'] = imgPath
    else:
        deleteList.append(ind)
        counter += 1
        print('ran', counter)
dataframe = dataframe.drop(dataframe.index[deleteList])
print(len(dataframe['Grade']))
dataframe.to_csv('DataSet_1.csv', index=False)
