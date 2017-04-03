import os
import matplotlib.pyplot as plt
import pickle



def decide_bins(n, vals):
    step = len(vals)/n
    base = 0
    bins = [vals[base]]
    left = n
    while left>0:
        base += step
        left -= 1
        bins += [vals[base]]
    
    bins[-1] = vals[-1] + 1
    return bins

def fetch_bins(n):
    files = [fil for fil in os.listdir('./bindata/') if fil.endswith('.csv')]
    vals = []
    for fil in files:
        f = open('./bindata/'+fil)
        lines = f.readlines()
        f.close()
        
        for idx, line in enumerate(lines):
            val = line.split(',')[1][1:-3]
            try:
                val = float(val)
            except:
                continue
            vals += [val]

    vals = sorted(vals)

    bins = decide_bins(n, vals)
    pickle.dump(bins, open('2048bins.pkl','w'))

fetch_bins(2048)
