import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np


data = pd.read_csv('./data/Iris.csv')

x = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

y = data.Species

le = LabelEncoder()


le.fit(y)

y = le.transform(y)

model = LinearRegression()
model.fit(x, y)

dataO = json.loads('{"firstObject": "firstVal"}')

dataA = json.loads('[{"firstObject": "firstVal"}]')

# assert type(dataO) == list

if type(dataA) is dict:
  print(type(dataO))
else:
  print('err')

print(type(dataA))

