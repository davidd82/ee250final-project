import pickle

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (10,7)
import seaborn as sns

from sklearn.model_selection import train_test_split

lounge = pd.read_csv("lounge.csv")

X = lounge[["sound","light"]].to_numpy()
y = lounge[["availability"]].to_numpy()

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X, y)
pickle.dump(clf, open("model.pickle","wb"))