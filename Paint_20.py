from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import mglearn
import pandas as pd
import random


x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
def calculator(res1, res2, res3, res4):
    l = list()
    for i in x_train:
        l.append(((i[2] - res3)**2 + (i[3] - res4)**2)**0.5)
    at = l.index(min(l))
    aa = y_train[at]
    at = l[at]
    l.remove(at)
    bt = l.index(min(l))
    ba = y_train[bt]
    bt = l[bt]
    l.remove(bt)
    ct = l.index(min(l))
    ca = y_train[ct]
    ct = l[ct]
    l.remove(ct)
    if ca != ba and aa != ca and ba != ca:
        return aa
    elif ba == aa or ba == ca:
        return ba
    elif aa == ca:
        return aa
count = 0
c = 0
for i in x_test:
    q = calculator(i[0], i[1], i[2], i[3])
    if q == y_test[count]:
        c += 1
    count += 1
print(c/count)
