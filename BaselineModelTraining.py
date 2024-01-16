# imports
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import SGDClassifier
from PIL import Image
import joblib
import BaselineModelGlobals as g


# initialization
with open('./Models and Preprocessors/BaselinePreprocessor', 'rb') as f:
    preprocessor = joblib.load(f)
classifier = SGDClassifier(loss='log_loss')

# training
g.divideDataToBatches(128, 128)
pix = []
epoch = 0
while True:
    print('EPOCH', epoch)
    counter = 0
    for ind, portion in enumerate(g.trainNamePortions):
        pix = []
        print(counter)
        for namePair in portion:
            im1 = Image.open(g.imgPath+'/'+namePair[0]).convert('L')
            im2 = Image.open(g.imgPath+'/'+namePair[1]).convert('L')
            pix.append(np.concatenate((np.asarray(im1), np.asarray(im2)), axis=0).flatten())
        processedBatch = preprocessor.transform(pix)
        classifier.partial_fit(processedBatch, g.trainGradePortions[ind], classes=g.uniqueGrades)
        counter += 1
    # model save
    name = './Models and Preprocessors/BaselineModelEpoch'+str(epoch)
    with open(name, 'wb') as f:
        joblib.dump(classifier, f)
    epoch += 1
