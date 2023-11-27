import pickle

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

with open("model.pickle", "rb") as f:
    # Load the classifier from the file
    clf = pickle.load(f)

lounge = pd.read_csv("loungetest.csv")

X = lounge[["sound","light"]].to_numpy()

print(round(np.mean(clf.predict(X))))