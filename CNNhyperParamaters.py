import torch
# Data globals
PRINT_DATA_INFO = False
UNIQUE_CLASSES = 29
IMAGE_PATH = './ImageAugment256x256'
IMAGE_DIMENSION = 256
COLOR_CHANNELS = 3
# training globals
PRINT_MODEL_SUMMARY = True
LEARNING_RATE = 2e-4
BATCH_SIZE = 32
EPOCHS = 1
accelerator = False
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    accelerator = True
