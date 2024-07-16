from d3blocks import D3Blocks
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\amber\Desktop\工作簿1.csv", usecols=[0, 1, 2])
df.columns = ['target', 'source','weight']
df = df.iloc[1:]
d3 = D3Blocks()

# 生成弦图
d3.chord(df)
