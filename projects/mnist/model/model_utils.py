import numpy as np
import torch
import streamlit as st


# Model definition
class MLP(torch.nn.Module):

    # Constructor
    def __init__(self, D_i=784, H=100, D_out=10):

        # Super constructor
        super(MLP, self).__init__()

        # Layers
        self.fc1 = torch.nn.Linear(D_i, H)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(H, D_out)

    # Forward pass
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
    

st.cache_resource()
def load_model():
    model = torch.load("projects/mnist/model/model.pth")
    model.eval()
    return model


def predict(model, image):
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