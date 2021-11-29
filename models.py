import data_create
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plot
import numpy as np
import math

def decision_tree(students, type, test_students, test_type):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(students, type)
    tree.plot_tree(clf, filled = True, rounded = True)
    plot.show()
    correct = 0
    predicted = clf.predict(test_students)
    for itr in range(len(predicted)):
        if predicted[itr] == test_type[itr]:
            correct += 1
    print(correct / len(test_students))

def random_forest(students, type, test_students, test_type):
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(students, type)
    correct = 0
    predicted = clf.predict(test_students)
    for itr in range(len(predicted)):
        if predicted[itr] == test_type[itr]:
            correct += 1
    print(correct / len(test_students))

def Gaussian_naieve_bayes(students, type, test_students, test_type):
    predicted = GaussianNB().fit(students, type).predict(test_students)
    correct = 0
    for itr in range(len(predicted)):
        if predicted[itr] == test_type[itr]:
            correct += 1
    print(correct / len(test_students))

if __name__ =='__main__':
    student_list = []
    test_list =[]
    find = 0
    #np.random.seed(12)
    for i in range(10000):
        student_list.append(data_create.create_student())
    student_type = data_create.classify_student(student_list)
    for i in range(100):
        test_list.append(data_create.create_student())
    test_student_type = data_create.classify_student(student_list)
    for itr in range(len(student_type)):
        if student_type[itr] == 1:
            find += 1
    print(find)
    decision_tree(student_list, student_type, test_list, test_student_type)
    random_forest(student_list, student_type, test_list, test_student_type)
    Gaussian_naieve_bayes(student_list, student_type, test_list, test_student_type)

