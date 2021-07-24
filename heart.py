import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt

# LOADING DATASET

test = pd.read_csv('heart/test.csv')
train = pd.read_csv('heart/train.csv')
data = pd.read_csv('heart/heart.csv')

ch = []
ch2 = []
ch3 = []
chol = data['chol']
chol2 = test['chol']
chol3 = train['chol']
cl = chol.values.tolist()
cl2 = chol2.values.tolist()
cl3 = chol3.values.tolist()

# SETTING SEED

np.random.seed(8)

# DATA PREPROCESSING

for i in range(0, len(cl), 1):
    if (cl[i] <= 180):
        ch.append(0)
    elif cl[i] > 180 and cl[i] <= 220:
        ch.append(1)
    else:
        ch.append(2)

for i in range(0, len(cl2), 1):
    if (cl2[i] <= 180):
        ch2.append(0)
    elif cl2[i] > 180 and cl2[i] <= 220:
        ch2.append(1)
    else:
        ch2.append(2)

for i in range(0, len(cl3), 1):
    if (cl3[i] <= 180):
        ch3.append(0)
    elif cl3[i] > 180 and cl3[i] <= 220:
        ch3.append(1)
    else:
        ch3.append(2)
data['nchol'] = ch
test['nchol'] = ch2
train['nchol'] = ch3

age = data['age']
age2 = test['age']
age3 = train['age']
ag = []
ag2 = []
ag3 = []
ab = age.values.tolist()
ab2 = age2.values.tolist()
ab3 = age3.values.tolist()

for i in range(0, len(ab), 1):
    if (ab[i] <= 30):
        ag.append(0)
    elif (ab[i] > 30 and ab[i] <= 50):
        ag.append(1)
    else:
        ag.append(2)
for i in range(0, len(ab2), 1):
    if (ab2[i] <= 30):
        ag2.append(0)
    elif (ab2[i] > 30 and ab2[i] <= 50):
        ag2.append(1)
    else:
        ag2.append(2)

for i in range(0, len(ab3), 1):
    if (ab3[i] <= 30):
        ag3.append(0)
    elif (ab3[i] > 30 and ab3[i] <= 50):
        ag3.append(1)
    else:
        ag3.append(2)
data['nage'] = ag
test['nage'] = ag2
train['nage'] = ag3

# SPLITTING INTO TRAINING AND TESTING

train = train.drop(['age', 'chol'], axis=1)
test = test.drop(['age', 'chol'], axis=1)
data = data.drop(['age', 'chol'], axis=1)

y = data['target'].values.tolist()
x = data.drop('target', axis=1)

x_train = train.drop('target', axis=1)
x_test = test.drop('target', axis=1)
y_train = train['target'].values.tolist()
y_test = test['target'].values.tolist()

# TRYING VARIOUS MODEL

# KNN CLASSIFIER

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
yknn = knn.predict(x_test)
metrics.accuracy_score(y_test, yknn)  # 0.81

# NAIVE BAYES CLASSIFIER

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb.fit(x_train, y_train)
ynb = nb.predict(x_test)
metrics.accuracy_score(y_test, ynb)  # 0.9

# SUPPORT VECTOR MACHINE CLASSIFIER

from sklearn import svm

support = svm.SVC(kernel='linear')
support.fit(x_train, y_train)
ysvm = support.predict(x_test)
metrics.accuracy_score(y_test, ysvm)  # 0.91

# RANDOM FOREST CLASSIFIER

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)
clf.fit(x_train, y_train)
ypre = clf.predict(x_test)
metrics.accuracy_score(y_test, ypre)  # 0.85

# DECISION TREE CLASSIFIER

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion="entropy", max_depth=3)
dtc.fit(x_train, y_train)
ydtc = dtc.predict(x_test)
metrics.accuracy_score(y_test, ydtc)  # 0.81

# LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state=0, max_iter=500)
lr.fit(x_train, y_train)
ylr = lr.predict(x_test)
metrics.accuracy_score(y_test, ylr)  # 0.92
'''
diction = {'Actual Disease': y_test, 'Predicted Disease': ylr}
report = pd.DataFrame(diction)
report.to_csv('heart_report.csv', index=True, header=True)
'''

plt.hist([y_test, ylr])
plt.title("HEART")
plt.xlabel("OUTPUT")
plt.ylabel("FREQUENCY")
plt.legend(labels=['Actual value', 'Predicted value'])
plt.show()


def heartop(m, c, rbp, fbs, ec, mha, ea, op, s, mv, t, ichol, iage):
    inputtest = [m, c, rbp, fbs, ec, mha, ea, op, s, mv, t, ichol, iage]
    predict = lr.predict([inputtest])
    predicted = predict[0]
    return predicted
