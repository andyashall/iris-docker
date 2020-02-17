import os
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Train model on startup
data = pd.read_csv('./data/Iris.csv')
x = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data.Species
le = LabelEncoder()
le.fit(y)
y = le.transform(y)
model = RandomForestClassifier()
model.fit(x, y)
print('Trained')

@app.route('/predict', methods=['POST'])
def predict():
  # Get the request body
  data = request.json

  # Check if data is a dict or list 
  if type(data) is list:
    # Feel free to add the code to to return multiple predictions
    return('Please just provide one example')
  else:
    # Need to add type checking and property name check

    # This is where all the data transformation would be
    data = pd.DataFrame(data, index=[0])
    print(data)
    pred = model.predict(data)
    print(pred)
    label = le.inverse_transform(pred)
    prob = model.predict_proba(data)
    # print()
    # return 'a'
    return jsonify(label = label[0], proba = prob[0][pred[0]])


@app.route('/', methods=['GET'])
def root():
  return render_template('index.html')

if __name__ == "__main__":
  # train_model()
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True,host='0.0.0.0',port=port)

