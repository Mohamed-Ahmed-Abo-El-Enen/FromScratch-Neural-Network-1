import numpy as np
import matplotlib.pyplot as plt
import sklearn
import sklearn.datasets
import sklearn.linear_model
from planar_utils import plot_decision_boundary, sigmoid, load_planar_dataset, load_extra_datasets

X, Y = load_planar_dataset()

plt.scatter(X[0, :], X[1, :], c=Y[0, :], s=40, cmap=plt.cm.get_cmap("Spectral"))
plt.show()

shape_X = X.shape
shape_Y = Y.shape
m = X.shape[1]

clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X.T, Y.T)

plot_decision_boundary(lambda x: clf.predict(x), X, Y)
plt.title("Logistic Regression")
plt.show()

LR_predictions = clf.predict(X.T)
print('Accuracy of logistic regression: %d ' % float((np.dot(Y, LR_predictions) + np.dot(1-Y, 1-LR_predictions))/float(Y.size)*100) +
       '% ' + "(percentage of correctly labelled data points)")

