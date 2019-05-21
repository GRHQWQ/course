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
# from sklearn.metrics import confusion_matrix,average_recall_score,average_precision_score,accuracy_score,f1_score
# confusion = confusion_matrix(y_test,y_predict)
# recall = average_recall_score(y_test, y_predict)
# precision = average_precision_score(y_test, y_predict)
# accuracy = accuracy_score(y_test, y_predict)
# f1 = f1_score(y_test, y_predict)
# print(confusion)
# print(recall)
# print(precision)
# print(f1)
# print(accuracy)
from sklearn.metrics import precision_recall_fscore_support
precision_recall_fscore_support = precision_recall_fscore_support(y_test, y_predict)
print(precision_recall_fscore_support)