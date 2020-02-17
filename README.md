# Iris Docker

A simple flask app to predict Iris subspecies based on Sepal and Petal length and width.

https://www.kaggle.com/uciml/iris

The app will listen on port 5000 and accept POST requests to /predict;

```js

{
  "SepalLengthCm": 2,
  "SepalWidthCm": 3,
  "PetalLengthCm": 1,
  "PetalWidthCm": 1
}

```

## Todo

- [ ] Handle multiple objects for prediction
- [ ] Create a train endpoint to save new datapoints and retrain model
- [ ] Tidy up front end
- [ ] Persist model in external file

## Get started

Clone the repo using `git clone https://gitlab.com/andyashall/iris-docker.git`

Login to the [Azure portal](portal.azure.com) and open the cloud shell and run the following commands to create a new resource group and a container registry for your app.

```sh
az group create --name iris-app --location uksouth

az acr create --resource-group iris-app --name iris-app --sku Basic
```

Login to [Azure Devops](dev.azure.com) and create a new project 



