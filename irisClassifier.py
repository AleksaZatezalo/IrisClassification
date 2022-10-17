import os
import matplotlib as plt
import pandas as pd

# Getting Iris Photos
s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
print('From URL: ', s)
df = pd.read_csv(s, header=None, encoding='utf-8')

# Getting first 100 Iris