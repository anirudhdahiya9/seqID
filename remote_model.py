from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
import os
import pickle
import numpy as np
import sys

windowsize = 100

def create_windows(data, step = 5):
    global windowsize
    windows = []
    for i in range(0, len(data) - windowsize + 1, 5):
        windows += [data[i:i+windowsize-1]]
    return windows

dr = './bindata/'
fils = ['Fault_1_case_1.csv.bins','Fault_2_case_1.csv.bins']
x = []
y = []
for fil in os.listdir(dr):
    if fil in fils:
        data = pickle.load(open(dr + fil))
        data = data - 1
        windows = create_windows(data)
        if fil ==fils[0]:
            ans = [1]*len(windows)
        else:
            ans = [0]*len(windows)
        x += windows
        y += ans

x_test = []
y_test = []
x_train = []
y_train = []
for i in range(len(x)):
    if i%5==0:
        x_test.append(x[i])
        y_test.append(y[i])
    else:
        x_train.append(x[i])
        y_train.append(y[i])

print 'test train sizes'
print len(x_train), len(y_train)
print len(x_test), len(y_test)


x_train = np.matrix(x_train)
x_test = np.matrix(x_test)

max_features = 2048
model = Sequential()
model.add(Embedding(max_features, output_dim=128))
model.add(LSTM(64))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))

'''
filepath="weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.compile(loss='binary_crossentropy',optimizer='rmsprop', metrics=['accuracy'])
'''

filename = sys.argv[1]
model.load_weights(filename)
model.compile(loss='binary_crossentropy',optimizer='rmsprop', metrics=['accuracy'])


#model.fit(x_train, y_train, batch_size=16, epochs=10, callbacks=callbacks_list)
score = model.evaluate(x_test, y_test, batch_size=16)

print score
