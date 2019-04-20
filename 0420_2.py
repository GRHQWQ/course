import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris =  datasets.load_iris()
# 数据集两部分：data和label
iris_X = iris.data
iris_y = iris.target

from sklearn.neighbors import KNeighborsClassifier
#定义一个变量，这个变量就是这个类的具体形式

knn = KNeighborsClassifier(n_neighbors=3)

from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_neighbors':[3,4,5],
    
}
gs =GridSearchCV(knn,param_grid,scoring='accuracy',cv=5,verbose=2)
gs.fit(iris_X,iris_y)
print(gs.best_params_, gs.best_score_)