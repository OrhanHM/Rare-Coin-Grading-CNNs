import pandas as pd
from PIL import Image
import urllib3
import os
from time import sleep


dataframe = pd.read_csv('realDataSet.csv')
http = urllib3.PoolManager(retries=urllib3.util.Retry(5, backoff_factor=1))

for i in range(80801, 91821):
    run = True
    print(i)
    resp = http.request('GET', dataframe.at[i, 'Image Link']).data
    counter = 0
    while len(resp) < 10000 and counter < 3:
        print('ran', counter)
        sleep(1)
        resp = http.request('GET', dataframe.at[i, 'Image Link']).data
        counter += 1
    if len(resp) < 10000:
        run = False
    if run:
        filename = 'img'+str(i+1)+'.jpg'
        path = '/Volumes/Toshiba/RawImages/'+filename
        with open(filename, 'wb') as f:
            f.write(resp)
            f.close()
        im = Image.open(filename).resize((4000, 2000))
        im.save(path)
        os.remove(filename)


# dataframe.to_csv('dataSetWithImgNames.csv', index=False)
