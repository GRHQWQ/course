import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris =  datasets.load_iris()
# 数据集两部分：data和label
iris_X = iris.data
iris_y = iris.target
# print(iris_X)
# print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
# 训练部分：X_train y_train
# 测试：X_test y_test

from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train,y_train)
y_predict = svm.predict(X_test)

print('y_predict',y_predict)
print('y_test',y_test)
#预测准确率  
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_predict)
print(accuracy)