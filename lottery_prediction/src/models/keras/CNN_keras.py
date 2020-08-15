from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers import Dense, Flatten, MaxPooling2D, Activation, Dropout, BatchNormalization
from keras.optimizers import Adam
import numpy as np
import src.preprocessingData.CrossMatrix1 as crossMatrix
from keras import backend as K
import matplotlib.pyplot as plt
K.tensorflow_backend._get_available_gpus()

np.random.seed(42)

matrix = crossMatrix.CrossMatrix1()
train_x, train_y, pred_x = matrix.splitTrain()

model = Sequential()
model.add(Conv2D(4, (3, 3), padding='same', activation='relu', input_shape=(45,45,3)))
model.add(BatchNormalization())
model.add(Conv2D(4, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(2,2))
#model.add(Dropout(rate=0.2))

model.add(Conv2D(8, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(8, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(16, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(16, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(2,2))
#model.add(Dropout(rate=0.3))

model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(2,2))
#model.add(Dropout(rate=0.4))

model.add(Flatten())
model.add(Dense(1000, activation='relu'))
#model.add(Dropout(rate=0.5))
model.add(Dense(500, activation='relu'))
model.add(Dense(45))
model.add(Activation('softmax'))
optimizer = Adam(lr=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['acc'])

model.summary()

history = model.fit(train_x, train_y, epochs=60, batch_size=64)
#model.fit(train_x, train_y, epochs=300, batch_size=32, validation_split=0.2)
pred_y = model.predict(pred_x)

predictNumber = []

for i in range(6):
    predictNumber.append(np.argmax(pred_y))
    pred_y[0, predictNumber[i]] = 0
    predictNumber[i] = predictNumber[i] + 1
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