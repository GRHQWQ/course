# 标准化数据模块
from sklearn import preprocessing 
import numpy as np

# 将资料分割成train与test的模块
from sklearn.model_selection import train_test_split

# 生成适合做classification资料的模块
from sklearn.datasets.samples_generator import make_classification 

# Support Vector Machine中的Support Vector Classifier
from sklearn.svm import SVC 

# 可视化数据的模块
import matplotlib.pyplot as plt 

from sklearn.metrics import accuracy_score

from sklearn.preprocessing import scale

#生成具有2种属性的300笔数据
X, y = make_classification(
    n_samples=300, n_features=2,
    n_redundant=0, n_informative=2, 
    random_state=21, n_clusters_per_class=1, 
    scale=100)

#可视化数据
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
flq = SVC()
flq.fit(X_train, y_train)

accuracy1 = flq.score(X_test, y_test)

y_predict = flq.predict(X_test)
accuracy = accuracy_score(y_test, y_predict)

print(accuracy)
print(accuracy1)

preprocessed_X = scale(X)
X_train, X_test, y_train, y_test = train_test_split(preprocessed_X, y, test_size=0.3)
flq = SVC()
flq.fit(X_train, y_train)

accuracy1 = flq.score(X_test, y_test)
print(accuracy1)

