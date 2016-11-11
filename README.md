# DataScience

Project source can be found from Youtube:

Introduction - Learn Python for Data Science #1 created by Sirajology

Youtube URL: (https://www.youtube.com/watch?v=T5pRlIbr6gg&index=1&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)


## Author: Weijie

```
Day_1_GenderClassifier.py

README.md
```

## Dependencies

* scikit (http://scikit-learn.org/)


## Usage

Once you have your dependencies installed via pip, run the script in terminal via

```
python Day_1_GenderClassifier.py
```

## Challenge

1. Use any 3 SciKit-Learn Models on the dataset below
2. Compare results
3. Print the best one

## Module imported

```
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
```

## DataSet
```
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
```

## Classified Models used in the sample
* Decision Tree
* KNeighborsClassifier
* linearSVM
* AdaBoostClassifier


  