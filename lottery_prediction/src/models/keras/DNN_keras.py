import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
import numpy as np
np.random.seed(70000)
import csv
counts = 850
counts = counts - 1
xtrain = np.zeros((int(counts/2), 45))
ytrain = np.zeros((int(counts/2), 45))
test = []
with open('/Users/hangeulbae/Desktop/deeplearningLo/src/lotto_val.csv', 'r') as f:
    reader = csv.reader(f)
    count = 0
    xindex = 0
    yindex = 0
    for row in reader:
        if (count < counts):
            if ((count % 2) == 0):
                xtrain[xindex] = np.array(row[1:46])
                xindex = xindex + 1
                count = count + 1
            else:
                ytrain[yindex] = np.array(row[1:46])
                yindex = yindex + 1
                count = count + 1
        else:
            test = np.asarray(row[1:46])
f.close()
xtrain = xtrain.astype('int32')
ytrain = ytrain.astype('int32')
test = test.astype('int32')
test = test.reshape(1, 45)  # 모양을 1,45행렬로 해야됨 그냥 45로 하면 오류 남 should make matrix wit two dimension
model = Sequential()
model.add(Dense(90, activation='relu', input_dim=45))
model.add(BatchNormalization())
model.add(Dense(60, activation='relu'))
model.add(BatchNormalization())
# model.add(Dense(360, activation='relu'))
# model.add(Dense(360, activation='relu'))
# model.add(Dense(360, activation='relu'))
# model.add(Dense(360, activation='relu'))
# model.add(Dense(360, activation='relu'))
# model.add(Dense(360, activation='relu'))
model.add(Dense(45, activation='sigmoid'))
model.compile(optimizer='adam',loss='mse')
model.fit(xtrain, ytrain, epochs=300, batch_size=200)
yhat = model.predict(test)
print(yhat.size)
print(yhat)
print(test)
max = []
for i in range(6):
    max.append(np.argmax(yhat))
    yhat[0, max[i]] = 0
    max[i] = max[i] + 1
max.sort()
print(max)
