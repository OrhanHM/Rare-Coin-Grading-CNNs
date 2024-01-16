from time import time
import CNNhyperParamaters as h
import CNNdataPrep as d
import CNNmodelPrep as m
import torch


trainSteps = len(d.train_dataloader.dataset)//h.BATCH_SIZE
start = time()
for e in range(h.EPOCHS):
    m.cnn.train()

    totalTrainLoss = 0
    trainCorrect = 0
    step = 0
    for (x, y) in d.train_dataloader:
        if step % 10 == 0:
            print(step)
            if step == 300:
                preds = []
                miniPredBatch = list(pred.argmax(1))
                for i in miniPredBatch:
                    preds.append(int(i))
                print(preds)

        y = y.to(h.mps_device)

        start = time()
        pred = m.cnn(x)
        loss = m.lossFn(pred, y)
        end = time()
        print(round(end-start, 2))

        start = time()
        m.opt.zero_grad()
        loss.backward()
        m.opt.step()
        end = time()
        print(round(end-start, 2))
        print()

        totalTrainLoss += loss
        trainCorrect += (pred.argmax(1) == y).type(
            torch.float).sum().item()

        step += 1

    trainAcc = trainCorrect/len(d.train_dataloader.dataset)
    trainLoss = totalTrainLoss/trainSteps
    print('Accuracy', round(100*trainAcc, 2), 'percent')
    print('Loss', trainLoss)

end = time()
print('Time', round(end-start, 2), 'seconds')

