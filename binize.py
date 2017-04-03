import pickle
import numpy as np
import os

bins = pickle.load(open('2048bins.pkl'))

bins = np.array(bins)
dr = './csvdata/'


for fil in os.listdir(dr):
    print fil
    ct = 0
    nct = 0
    data = []
    with open(dr + fil) as f:
        lines = f.readlines()
        for i, lin in enumerate(lines):
            try:
                data += [float(lin.split(',')[1][1:-3])]
            except Exception as e:
                #print e
                nct+=1
            ct+=1
    print nct, ct
    data = np.array(data)
    inds = np.digitize(data, bins)
    pickle.dump(inds, open(fil+'.bins', 'w'))

