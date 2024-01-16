import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import pickle

baseFolder = './Test Results/'
predFile = baseFolder + 'BaselineE5Preds'
gradeFile = baseFolder + 'BaselineActualGrades'

with open(predFile, 'rb') as f:
    yPreds = pickle.load(f)
with open(gradeFile, 'rb') as f:
    yActual = pickle.load(f)

cm = metrics.confusion_matrix(yActual, yPreds)
newCm = np.zeros((5, 5), dtype=int)

buckets = [[1, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28]]
bucketNames = ['1 to 8', '10 to 30', '35 to 55', '58 to 65', '66 to 70']
numBuckets = len(buckets)
for ind1, vals1 in enumerate(buckets):
    for ind2, vals2 in enumerate(buckets):
        total = 0
        for i in vals1:
            for j in vals2:
                total += cm[i][j]
        newCm[ind1][ind2] = int(total)


plt.figure(figsize=(10, 10))
plt.imshow(newCm, interpolation='nearest', cmap='Pastel1')
plt.title('Confusion matrix', size=15)
plt.colorbar()
tick_marks = np.arange(numBuckets)
plt.xticks(tick_marks, bucketNames, rotation=45, size=10)
plt.yticks(tick_marks, bucketNames, size=10)
plt.tight_layout()
plt.ylabel('Actual label', size=15)
plt.xlabel('Predicted label', size=15)
width, height = newCm.shape
for x in range(numBuckets):
    for y in range(numBuckets):
        plt.annotate(str(newCm[x][y]), xy=(y, x),
                     horizontalalignment='center',
                     verticalalignment='center')
plt.show()
