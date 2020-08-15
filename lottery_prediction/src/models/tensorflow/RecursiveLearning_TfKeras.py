import numpy as np
import matplotlib.pyplot as plt
import src.preprocessingData.CrossMatrix1 as crossMatrix
import tensorflow as tf

matrix = crossMatrix.CrossMatrix1()
train_x, train_y, pred_x = matrix.splitTrain()

input_data = tf.keras.Input(name='input', shape=(45,45,3))
conv1 = tf.keras.layers.Conv2D(16, (3,3), padding='same',
            activation='relu', name='CONV2D_1')(input_data)
conv1_b = tf.keras.layers.BatchNormalization()(conv1)
conv2 = tf.keras.layers.Conv2D(16, (3,3), padding='same',
            activation='relu', name='CONV2D_2')(conv1_b)
conv2_b = tf.keras.layers.BatchNormalization()(conv2)
conv3 = tf.keras.layers.Conv2D(16, (3,3), padding='same',
            activation='relu', name='CONV2D_3')(conv2_b)
conv3_b = tf.keras.layers.BatchNormalization()(conv3)
conv4 = tf.keras.layers.Conv2D(16, (3,3), padding='same',
            activation='relu', name='CONV2D_4')(conv3_b)
conv4_b = tf.keras.layers.BatchNormalization()(conv4)
fx_x = tf.keras.layers.Add()([conv1,conv4_b])
#dropout = Dropout(rate=0.5)(fx_x)
flatten_layer = tf.keras.layers.Flatten()
flatten = flatten_layer(fx_x)

dense1 = tf.keras.layers.Dense(1000, activation='relu',
            name='DENSE_1')(flatten)
dense1_b = tf.keras.layers.BatchNormalization()(dense1)
dense2 = tf.keras.layers.Dense(500, activation='relu',
            name='DENSE_2')(dense1_b)
y_pred = tf.keras.layers.Dense(45, activation='softmax',
            name='DENSE_3')(dense2)

#y_pred = Activation('softmax',name='softmax')(dense3)

model = tf.keras.models.Model(inputs=input_data, outputs=y_pred)

print(model.summary())
#optimizer = Adam(lr=0.000001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
optimizer = tf.keras.optimizers.Adam(lr=0.000001)
model.compile(loss='categorical_crossentropy',optimizer=optimizer, metrics=['acc'])
history = model.fit(train_x, train_y, epochs=190, batch_size=64)
pred_y = model.predict(pred_x)
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