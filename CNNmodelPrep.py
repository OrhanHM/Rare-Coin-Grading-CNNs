import torch
from torch import flatten, nn
from torch.nn import Module, Conv2d, Linear, MaxPool2d, ReLU, LogSoftmax
from torch.optim import Adam
from torchsummary import summary
import CNNhyperParamaters as h


#  MODEL CLASS DEFINITION
class LeNet(Module):
    def __init__(self, numChannels, classes, device):
        # call the parent constructor
        super(LeNet, self).__init__()

        self.device = device

        self.conv1 = Conv2d(in_channels=numChannels, out_channels=20,
                            kernel_size=(5, 5))
        self.relu1 = ReLU()
        self.maxpool1 = MaxPool2d(kernel_size=(2, 2), stride=(2, 2))

        self.conv2 = Conv2d(in_channels=20, out_channels=50,
                            kernel_size=(5, 5))
        self.relu2 = ReLU()
        self.maxpool2 = MaxPool2d(kernel_size=(2, 2), stride=(2, 2))

        '''self.conv3 = Conv2d(in_channels=35, out_channels=50,
                            kernel_size=(5, 5))
        self.relu3 = ReLU()
        self.maxpool3 = MaxPool2d(kernel_size=(2, 2), stride=(2, 2))'''

        # possibilities:
        # 50 channels, 2 Maxpool x2: 381250
        # 50 channels, 2 Maxpool x3: 84000
        self.fc1 = Linear(in_features=381250, out_features=500)
        self.relu4 = ReLU()

        self.fc2 = Linear(in_features=500, out_features=classes)
        self.logSoftmax = LogSoftmax(dim=1)

    def forward(self, x):

        x = x.to(self.device)
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.maxpool1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.maxpool2(x)

        '''x = self.conv3(x)
        x = self.relu3(x)
        x = self.maxpool3(x)'''

        x = flatten(x, 1)
        x = self.fc1(x)
        x = self.relu4(x)

        x = self.fc2(x)
        output = self.logSoftmax(x)
        return output


# MODEL INITIALIZATION
if h.accelerator:
    cnn = LeNet(numChannels=h.COLOR_CHANNELS, classes=h.UNIQUE_CLASSES, device=h.mps_device).to(h.mps_device)
    print("SUCCESSFUL ACCELERATION IMPLEMENTATION")
else:
    cnn = LeNet(numChannels=h.COLOR_CHANNELS, classes=h.UNIQUE_CLASSES, device=torch.device("cpu"))
    print("UNSUCCESSFUL ACCELERATION IMPLEMENTATION")


if h.PRINT_MODEL_SUMMARY:
    summary(cnn, (h.COLOR_CHANNELS, h.IMAGE_DIMENSION, h.IMAGE_DIMENSION*2))


opt = Adam(cnn.parameters(), lr=h.LEARNING_RATE)
lossFn = nn.NLLLoss()
