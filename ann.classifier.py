import numpy as np
from sklearn.model_selection import train_test_split
dataset = np.load('final-dobara.npy')
from keras import optimizers
X = dataset[:,:-1]
y = dataset[:, -1]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

from keras.models import Sequential 
from keras.layers import Dense, Activation 
output_dim = nb_classes =2
from keras.utils import np_utils 
Y_train = np_utils.to_categorical(y_train, nb_classes) 
Y_test = np_utils.to_categorical(y_test, nb_classes)
input_dim = len(X[0])
model = Sequential() 
model.add(Dense(output_dim, input_dim=9, activation='softmax')) 
batch_size = 62 
nb_epoch = 200 
sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
from keras import metrics
model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=[metrics.categorical_accuracy, 'accuracy'])
history = model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch,verbose=1, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=0) 
print(score)
