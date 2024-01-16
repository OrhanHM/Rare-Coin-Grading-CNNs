# imports
import numpy as np
import sklearn
from PIL import Image
import joblib
import BaselineModelGlobals as g

with open('./Models and Preprocessors/BaselinePreprocessor', 'rb') as f:
    preprocessor = joblib.load(f)
with open('./Models and Preprocessors/BaselineModelEpoch5', 'rb') as f:
    classifier = joblib.load(f)

# making predictions
g.divideDataToBatches(5000, 5000)
counter = 0
preds = []
grades = []
for ind, portion in enumerate(g.testNamePortions):
    pix = []
    print(counter)
    for namePair in portion:
        im1 = Image.open(g.imgPath+'/'+namePair[0]).convert('L')
        im2 = Image.open(g.imgPath+'/'+namePair[1]).convert('L')
        pix.append(np.concatenate((np.asarray(im1), np.asarray(im2)), axis=0).flatten())
    processedBatch = preprocessor.transform(pix)
    batchPreds = classifier.predict(processedBatch)
    for i, val in enumerate(batchPreds):
        preds.append(val)
        grades.append(g.testGradePortions[ind][i])
    counter += 1

with open('./Test Results/BaselineE5Preds', 'wb') as f:
    joblib.dump(preds, f)
with open('./Test Results/BaselineActualGrades', 'wb') as f:
    joblib.dump(grades, f)
