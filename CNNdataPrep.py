import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
import torch
from torchvision.io import read_image
from torch.utils.data import Dataset, DataLoader
import CNNhyperParamaters as h


# input = pytorch image tensor
def displayImage(imgTensor):
    plt.imshow(imgTensor.permute(1, 2, 0))
    plt.show()


# IMAGE DATASET CLASS DEFINITION, used separately for train and test datasets
class CustomImageDataset(Dataset):
    def __init__(self, labels, names, img_dir):
        self.img_labels = labels
        self.img_names = names
        self.img_dir = img_dir

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_names.iloc[idx, 0])
        image1 = read_image(img_path)
        img_path = os.path.join(self.img_dir, self.img_names.iloc[idx, 1])
        image2 = read_image(img_path)
        image = torch.cat((image1, image2), 2)/255
        label = self.img_labels[idx]
        return image, label


# DATASET GLOBALS
filenames = os.listdir(h.IMAGE_PATH)
imagenames = [name for name in filenames if name.endswith('.jpg')]
totalImages = len(imagenames)
labelData = pd.read_csv('NewFinalDataframe.csv')
trainNames, testNames, trainGradeSeries, testGradeSeries = train_test_split(labelData[['Large Obverse Path', 'Large Reverse Path']], labelData['Grade'], random_state=1, test_size=0.25)

trainLen = len(trainGradeSeries)
testLen = len(testGradeSeries)

# PRINTING DATA INFO
if h.PRINT_DATA_INFO:
    print('Total Images:', totalImages)
    print('Total Data Points:', len(labelData))
    print('Unique Grades:', h.UNIQUE_CLASSES)
    print()
    print('Training Data Points:', trainLen)
    print('Test Data Points:', testLen)
    print()

# MAP GRADES 1-70 TO LABELS 0-28
label_map = {
    1: 0, 2: 1, 3: 2, 4: 3, 6: 4, 8: 5, 10: 6, 12: 7, 15: 8, 20: 9, 25: 10,
    30: 11, 35: 12, 40: 13, 45: 14, 50: 15, 53: 16, 55: 17, 58: 18, 61: 19, 62: 20,
    63: 21, 64: 22, 65: 23, 66: 24, 67: 25, 68: 26, 69: 27, 70: 28
}
interList = list(trainGradeSeries)
trainGrades = [label_map[i] for i in interList]

interList = list(testGradeSeries)
testGrades = [label_map[i] for i in interList]
del interList

# DATASET AND DATALOADER INITIALIZATION
train_dataset = CustomImageDataset(trainGrades, trainNames, h.IMAGE_PATH)
test_dataset = CustomImageDataset(testGrades, testNames, h.IMAGE_PATH)

train_dataloader = DataLoader(train_dataset, batch_size=h.BATCH_SIZE, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=h.BATCH_SIZE, shuffle=False)

# IMAGE DISPLAY TEST CODE
'''data = train_dataset.__getitem__(6)
im = data[0]
gradeLabel = data[1]
print(gradeLabel)
displayImage(im)'''

# DATALOADER ITER TEST CODE
'''train_features, train_labels = next(iter(train_dataloader))
print(train_features.shape)
print(train_labels)'''
