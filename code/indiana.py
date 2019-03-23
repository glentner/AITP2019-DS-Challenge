import pandas as pd

dtypes = {'1':'str', '2':'str', '3':'str', '4':'str', '5':'str', '6':'str'};

for chunk in pd.read_csv('./data/gsod.obs.csv', chunksize=(10 ** 6), dtype=dtypes):
    for i in range(0,chunk.shape):
        ref = chunk.ix[i]
        if(ref[0] == '999999'):
            ref.to_csv(testCSV.csv, index=False, header=False, mode='a')