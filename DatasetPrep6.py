import pandas as pd

dataframe = pd.read_csv('NewFinalDataframe.csv')[['Grade', 'Large Obverse Path', 'Large Reverse Path']]
dataframe.to_csv('NewFinalDataframe.csv', index=False)
