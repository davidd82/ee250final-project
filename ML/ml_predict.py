import pickle

import numpy as np
import pandas as pd

import sys 
import os

from sklearn.model_selection import train_test_split

def predict():
    with open("model.pickle", "rb") as f:
        # Load the classifier from the file
        clf = pickle.load(f)

    lounge = pd.read_csv("../data-points.csv")

    X = lounge[["sound","light"]].to_numpy()

    prediction = round(np.mean(clf.predict(X)))
    print(prediction) # we will encrypt this

    return prediction
