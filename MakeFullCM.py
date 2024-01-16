import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import joblib


baseFolder = './Test Results/'
predFile = baseFolder + 'BaselineE5Preds'
gradeFile = baseFolder + 'BaselineActualGrades'

with open(predFile, 'rb') as f:
    yPreds = joblib.load(f)
with open(gradeFile, 'rb') as f:
    yActual = joblib.load(f)

acc = metrics.accuracy_score(yActual, yPreds)
print('Accuracy:', round(acc*100, 2))
cm = metrics.confusion_matrix(yActual, yPreds)

numGrades = 29
grades = [i for i in range(numGrades)]

plt.figure(figsize=(15, 15))
plt.imshow(cm, interpolation='nearest', cmap='Pastel1')
plt.title('Confusion matrix', size=15)
plt.colorbar()
tick_marks = np.arange(numGrades)
plt.xticks(tick_marks, grades, rotation=45, size=10)
plt.yticks(tick_marks, grades, size=10)
plt.tight_layout()
plt.ylabel('Actual label', size=15)
plt.xlabel('Predicted label', size=15)
width, height = cm.shape
for x in range(numGrades):
    for y in range(numGrades):
        plt.annotate(str(cm[x][y]), xy=(y, x),
                     horizontalalignment='center',
                     verticalalignment='center')
plt.show()
