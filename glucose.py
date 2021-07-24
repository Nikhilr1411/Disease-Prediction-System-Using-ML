import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# SETTING SEED

np.random.seed(1)

# LOADING DATASET

data = pd.read_csv('diabetes/diabetes.csv')

# SPLITTING INTO TRAINING AND TESTING

y = data['Outcome'].values.tolist()
x = data.drop('Outcome', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# TRYING VARIOUS MODEL

# KNN CLASSIFIER

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
yknn = knn.predict(x_test)
accuracy_score(y_test, yknn)  # 0.75

# NAIVE BAYES CLASSIFIER

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb.fit(x_train, y_train)
ynb = nb.predict(x_test)
accuracy_score(y_test, ynb)  # 0.77

# SUPPORT VECTOR MACHINE CLASSIFIER

from sklearn import svm

support = svm.SVC(kernel='linear')
support.fit(x_train, y_train)
ysvm = support.predict(x_test)
accuracy_score(y_test, ysvm)  # 0.77

# DECISION TREE CLASSIFIER

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion="entropy", max_depth=3)
dtc.fit(x_train, y_train)
ydtc = dtc.predict(x_test)
accuracy_score(y_test, ydtc)  # 0.79

# LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state=0, max_iter=500)
lr.fit(x_train, y_train)
ylr = lr.predict(x_test)

accuracy_score(y_test, ylr)  # 0.77

# RANDOM FOREST CLASSIFIER

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)
clf.fit(x_train, y_train)
ypre = clf.predict(x_test)
accuracy_score(y_test, ypre)  # 0.83


def glucoseop(p, g, bp, s, i, bmi, dpf, a1):
    inputtest = [p, g, bp, s, i, bmi, dpf, a1]
    predict = clf.predict([inputtest])
    predicted = predict[0]
    return predicted
