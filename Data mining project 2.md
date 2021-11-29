###### tags: `data mining`
# Data mining project 2

## Goal - How to find a good student?
- Using three different classifiers to predict a given data is a good student or not ?
    - Decision tree
    - random forest
    - Naive Bayes
## Rules to create a student
- 1. study 0, 1
- 2. computer 0, 1
- 3. headphone 0, 1
- 4. play basketball 0, 1
- 5. screen 0, 1
- 6. assignments 0, 1
- 7. attend meeting 0, 1
- 8. listening music 0, 1
- 9. reading papers 0, 1
- 10. play computer games 0. 1
- 11. stream 0, 1
- 12. anime 0, 1
- 13. working day 0, 1, 2, 3, 4, 5, 6, 7
- 14. friends 0 ~ 49 ( intergers )
- 15. top conference : 0, 1, 2
- 16. beverage 0 ~ 2 (real number)
- 17. meal 1 ~ 5 ( intergers )
- 18. weight 50 ~ 99
- 19. shape 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- 20. height 150 ~ 189
## Rules to decide the student is good or not
- 1. study == 1 
- 2. computier == 1
- 9. reading papers == 1
- 13. working day > 5
- 15. top conference > 0
- 17. meal < 4 ( in experiment 2 this rule will be cancelled )
- 19. shape > 5 ( in experiment 2 this rule will be cancelled )

## Experiment 1
### Training the model 
- Create 10000 students to teach the classification model how to tell the difference between good students and normal students.
- There are six rules to determine whether a student is good or not.
### Testing the model 
- Create 100 students and let the model to decide which kind of student the person is.
### Outcome
#### Decision Tree
![](https://i.imgur.com/cMBMzX5.png)

The blue block stands for good student.

##### Comapare with the rules
- working day >= 5.5 ( The rule is set is working day > 5 )
- computer >= 0.5 ( The rule is set is computer == 1 )
- study >= 0.5 ( The rule is set is study == 1)
- reading papers >= 0.5 ( The rule is set is reading papers == 1 )
- shape >= 4.5 ( The rule is set is shape > 5)
- meals <= 3.5 ( The rule is set is meals < 4 )
- top conference >= 0.5 ( The rule is set is top conference > 0 )

Conclusion : The decision tree has find all the rules I gave. 

Test precision : 
![](https://i.imgur.com/OcbbSY1.png)
random seed : 12
#### Random Forest
Test precision : 
![](https://i.imgur.com/pufD0Yy.png)
random seed : 12
#### Naive Bayes
Test precision : 
![](https://i.imgur.com/fc3uFVs.png)
random seed : 12
### Conclusion of experiment 1
- The performance of Random Forest is better than Decision Tree.
- The performance of Decision Tree is better than Naive Bayes.


## Experiment 2
### Training the model 
- Create 10000 students to teach the classification model how to tell the difference between good students and normal students.
- There are only four rules to determine whether a student is good or not.
### Testing the model 
- Create 100 students and let the model to decide which kind of student the person is.
### Outcome
#### Decision Tree


The blue block stands for good student.

##### Comapare with the rules
- working day >= 5.5 ( The rule is set is working day > 5 )
- computer >= 0.5 ( The rule is set is computer == 1 )
- study >= 0.5 ( The rule is set is study == 1)
- reading papers >= 0.5 ( The rule is set is reading papers == 1 )
- top conference >= 0.5 ( The rule is set is top conference > 0 )

![](https://i.imgur.com/viJL2Ai.png)
Conclusion : The decision tree has find all the rules I gave. ( The same conclusion as experiment 1 )

Test precision : 
![](https://i.imgur.com/jtfhUpX.png)

random seed : 12
#### Random Forest
Test precision : 
![](https://i.imgur.com/oOahdQs.png)

random seed : 12
#### Naive Bayes
Test precision : 
![](https://i.imgur.com/fmQpUoF.png)

random seed : 12
### Conclusion of experiment 2
- The performance of Random Forest is better than Decision Tree.
- The performance of Decision Tree is better than Naive Bayes.


## Experiment 3
### Training the model 
- Create 50000 students to teach the classification model how to tell the difference between good students and normal students.
- There are six rules to determine whether a student is good or not.
### Testing the model 
- Create 100 students and let the model to decide which kind of student the person is.
### Outcome
#### Decision Tree


The blue block stands for good student.

##### Comapare with the rules
- working day >= 5.5 ( The rule is set is working day > 5 )
- computer >= 0.5 ( The rule is set is computer == 1 )
- study >= 0.5 ( The rule is set is study == 1)
- reading papers >= 0.5 ( The rule is set is reading papers == 1 )
- top conference >= 0.5 ( The rule is set is top conference > 0 )

![](https://i.imgur.com/LzUHrS4.png)

Conclusion : The decision tree has find all the rules I gave. ( The same conclusion as experiment 1 )

Test precision : 
![](https://i.imgur.com/PtyAxED.png)


random seed : 12
#### Random Forest
Test precision : 
![](https://i.imgur.com/21d0EuP.png)


random seed : 12
#### Naive Bayes
Test precision : 
![](https://i.imgur.com/cPuctg8.png)


random seed : 12
### Conclusion experiment 3
- The performance of Random Forest is equal to Decision Tree.
- The performance of Decision Tree is better than Naive Bayes.

## Experiment 4
### Training the model 
- Create 10000 students to teach the classification model how to tell the difference between good students and normal students.
- There are six rules to determine whether a student is good or not.
- Using 10 different random seed to repeat experiment 1. Try to find out that dataset will influent the performance of model or not.  
### Testing the model 
- Create 100 students and let the model to decide which kind of student the person is.
### Outcome

- Random seed = 1248
    - Test precision : 
        - Decision Tree : 0.99
        - Random Forest : 1.0
        - Naive Bayes : 0.96
- Random seed = 728
    - Test precision : 
        - Decision Tree : 0.99
        - Random Forest : 1.0
        - Naive Bayes : 0.94
- Random seed = 916
    - Test precision : 
        - Decision Tree : 0.99
        - Random Forest : 1.0
        - Naive Bayes : 0.94

- Random seed = 17389
    - Test precision : 
        - Decision Tree : 0.98
        - Random Forest : 0.99
        - Naive Bayes : 0.94

- Random seed = 48763
    - Test precision : 
        - Decision Tree : 0.99
        - Random Forest : 1.0
        - Naive Bayes : 0.9

- Random seed = 857
    - Test precision : 
        - Decision Tree : 1.0 
        - Random Forest : 1.0
        - Naive Bayes : 0.93

- Random seed = 4961
    - Test precision : 
        - Decision Tree : 0.97
        - Random Forest : 0.99
        - Naive Bayes : 0.91

- Random seed = 4285
    - Test precision : 
        - Decision Tree : 0.98
        - Random Forest : 0.99
        - Naive Bayes : 0.94

- Random seed = 3241
    - Test precision : 
        - Decision Tree : 0.99
        - Random Forest : 0.99
        - Naive Bayes : 0.94

- Random seed = 7098
    - Test precision : 
        - Decision Tree : 0.99
        - Random Forest : 0.99
        - Naive Bayes : 0.93
### Conclusion of experiment 4
- In average, the performance of Random Forest is better than Decision Tree. But some of the cases they have the same performance. So we can say that Random Forest is a better model in this task.
- The performance of Decision Tree is better than Naive Bayes. Naive Bayes is not a good choice for this task.

## Conclusion
- Comparing experiment 1 and experiment 2, we could know that more rules can let the model become more powerful.
- Comparing experiment 1 and experiment 3, we could know that more data can make the model doing much better while classifing a person is a good student or not. In other words, the model learn more from the dataset.
- In experiment 4, we could know that Random Forest is the best model for doing this task and Naive Bayes is the worst. 
