from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
import os
import pickle
import numpy as np

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

x = np.matrix(x)

max_features = 2048
model = Sequential()
model.add(Embedding(max_features, output_dim=128))
model.add(LSTM(64))
#model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='rmsprop', metrics=['accuracy'])

model.fit(x, y, batch_size=16, epochs=10)
score = model.evaluate(x, y, batch_size=16)

