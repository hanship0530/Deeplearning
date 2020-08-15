from __future__ import print_function
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt
import src.models.keras.Resnet as resnet
import src.preprocessingData.CrossMatrix1 as crossMatrix

from keras import backend as K
K.tensorflow_backend._get_available_gpus()

np.random.seed(42)

lr_reducer = ReduceLROnPlateau(factor=np.sqrt(0.1), cooldown=0, patience=5, min_lr=0.5e-6)
early_stopper = EarlyStopping(min_delta=0.001, patience=10)

batch_size = 32
nb_classes = 45
nb_epoch = 200

img_rows, img_cols = 45, 45
img_channels = 3

matrix = crossMatrix.CrossMatrix1()
X_train, Y_train, pred_x = matrix.splitTrain()

# Convert class vectors to binary class matrices.
# Y_train = np_utils.to_categorical(y_train, nb_classes)

X_train = X_train.astype('float32')

# subtract mean and normalize
mean_image = np.mean(X_train, axis=0)
X_train -= mean_image
X_train /= 128.

model = resnet.ResnetBuilder.build_resnet_18((img_channels, img_rows, img_cols), nb_classes)
optimizer = Adam(lr=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])

model.summary()

history = model.fit(X_train, Y_train,
          batch_size=batch_size,
          epochs=nb_epoch,
          callbacks=[lr_reducer, early_stopper])
# model.fit(X_train, Y_train,
#           batch_size=batch_size,
#           epochs=nb_epoch,
#           callbacks=[lr_reducer, early_stopper],
#           validation_split=0.25)

# model.fit(X_train, Y_train,
#           batch_size=batch_size,
#           nb_epoch=nb_epoch,
#           shuffle=True,
#           callbacks=[lr_reducer, early_stopper])

pred_y = model.predict(pred_x)

predictNumber = []

for i in range(6):
    predictNumber.append(np.argmax(pred_y))
    pred_y[0, predictNumber[i]]=0
    predictNumber[i]= predictNumber[i] + 1
predictNumber.sort()

print(predictNumber)

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