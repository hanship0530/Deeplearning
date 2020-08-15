
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, Flatten, BatchNormalization, Dropout, TimeDistributed
from keras.optimizers import Adam
import src.preprocessingData.CrossMatrix2 as crossMatrix
import matplotlib.pyplot as plt

import numpy as np

np.random.seed(42)

from keras import backend as K
K.tensorflow_backend._get_available_gpus()

mode = 1
dimension = 45
if(mode == 2):
    dimension = 6

matrix = crossMatrix.CrossMatrix2()
X, y, pred_x = matrix.splitTrain(mode=mode)

model = Sequential()
model.add(LSTM(dimension, input_shape=(1,dimension), return_sequences=True,
               stateful=False, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(rate=0.2))
model.add(LSTM(dimension, return_sequences=True, stateful=False, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(rate=0.3))
model.add(LSTM(dimension, stateful=False, activation='relu'))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(500, activation='relu'))
model.add(TimeDistributed(Dense(45, activation='softmax')))
optimizer = Adam(lr=0.001)
model.compile(optimizer=optimizer,loss='categorical_crossentropy', metrics=['acc'])

model.summary()
#에폭 300 이랑 500 하기
history = model.fit(X, y, epochs=300, batch_size=64)
# model.fit(train_x, train_y, epochs=300, batch_size=32, validation_split=0.25)
# model.fit(train_x, train_y, epochs=500, batch_size=32, validation_data=(test_x, test_y))
pred_y = model.predict(pred_x).reshape(1, 45)

predictNumber = []

for i in range(6):
    predictNumber.append(np.argmax(pred_y))
    pred_y[0, predictNumber[i]]=0
    predictNumber[i]= predictNumber[i] + 1
predictNumber.sort()

print(predictNumber)

# list all data in history
print(history.history.keys())
plt.figure(figsize=(500,300))
plt.subplot(2,1,1)
plt.plot(history.history['acc'], color='green')
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.subplot(2,1,2)
plt.plot(history.history['loss'], color='red')
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()