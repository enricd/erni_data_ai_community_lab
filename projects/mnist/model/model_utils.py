import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import streamlit as st


# Models definition
class MLP(nn.Module):

    # Constructor
    def __init__(self, D_i=784, H=100, D_out=10):

        # Super constructor
        super(MLP, self).__init__()

        # Layers
        self.fc1 = nn.Linear(D_i, H)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(H, D_out)

    # Forward pass
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
    

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
    

st.cache_resource()
def load_model(model_path):
    model = torch.load(model_path)
    model.eval()
    return model


def mlp_predict(model, image):
    # Convert the image to a tensor
    tensor = torch.from_numpy(image).float()

    # Add a batch dimension
    tensor = tensor.view(1, -1)

    # Get the model prediction
    prediction = model(tensor)

    # Get the index of the max log-probability
    pred = prediction.argmax(dim=1, keepdim=True)
    prediction = prediction[0]
    prediction = (prediction + abs(min(prediction))) / 1000
    prob = torch.nn.functional.softmax(prediction, dim=0)
    # print("prediction", prediction)
    # print("prob", prob)
    # print(sum(prob))

    return pred.item(), prob[pred.item()].item() * 100


def cnn_predict(model, image):
    # Convert the image to a tensor
    tensor = torch.from_numpy(image).float()

    # Add a batch dimension
    tensor = tensor.view(1, 28, 28)

    # Get the model prediction
    prediction = model(tensor)

    # Get the index of the max log-probability
    pred = prediction.argmax(dim=1, keepdim=True)
    prediction = prediction[0]
    prediction = (prediction + abs(min(prediction))) / 1000
    prob = torch.nn.functional.softmax(prediction, dim=0)
    # print("prediction", prediction)
    # print("prob", prob)
    # print(sum(prob))

    return pred.item(), prob[pred.item()].item() * 100