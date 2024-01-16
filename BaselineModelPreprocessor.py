# imports
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from PIL import Image
import joblib
import BaselineModelGlobals as g


# initialization
preprocessor = StandardScaler()

# fitting preprocessor
g.divideDataToBatches(1000, 1000)
counter = 0
for portion in g.trainNamePortions[:10]:
    pix = []
    print(str(counter)*10)
    minicounter = 0
    for namePair in portion:
        im1 = Image.open(g.imgPath+'/'+namePair[0]).convert('L')
        im2 = Image.open(g.imgPath+'/'+namePair[1]).convert('L')
        pix.append(np.concatenate((np.asarray(im1), np.asarray(im2)), axis=0).flatten())
        print(minicounter)
        minicounter += 1
    preprocessor.partial_fit(pix)
    counter += 1

with open('./Models and Preprocessors/BaselinePreprocessor', 'wb') as f:
    joblib.dump(preprocessor, f)
