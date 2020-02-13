# Iris Docker

A simple flask app to predict Iris subspecies based on Sepal and Petal length and width.

The app will listen on port 5000 and accept POST requests to /predict;

```js

{
  "SepalLengthCm": 2,
  "SepalWidthCm": 3,
  "PetalLengthCm": 1,
  "PetalWidthCm": 1
}

```