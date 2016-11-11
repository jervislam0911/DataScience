"""
Author: Weijie Lin

Following YouTube Challenge created by Sirajology

From Introduction - Learn Python for Data Science #1

"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier

# init Three different classifiers:
# 1. Decision Tree
# 2. KNeighborsClassifier
# 3. linearSVM
# 4. AdaBoostClassifier
classifiers = {'Decision Tree': DecisionTreeClassifier(), 'KNeighborsClassifier': KNeighborsClassifier(3), 'linearSVM': SVC(kernel='linear'),
               'AdaBoostClassifier': AdaBoostClassifier()}

# pre-defined data set:
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# my data set
my_data_set = [[192, 50, 43], [182, 57, 44], [176, 55, 34]]

# fit the model using X training data and y as target values
# Print prediction
for classifier_name, classifier_object in classifiers.items():
    classifier_object.fit(X, Y)
    print('{classifier_name}: {prediction}'
          .format(classifier_name=classifier_name, prediction=classifier_object.predict(my_data_set)))

