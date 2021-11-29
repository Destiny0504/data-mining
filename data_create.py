import numpy as np

# good master students
classes = { 'study': 1, 'play computer games': 0, 'reading papers': 1, 'height':178, 'play basketball' : 1,
            'weight': 75, 'shape': 10, 'computer': 1, 'headphones': 1, 'screen' : 1,
            'stream': 0, 'anime': 0, 'working day': 6, 'friends': 10, 'top conference' : 1,
            'beverage': 0.5, 'meal': 3, 'assignments': 1, 'attend meeting': 1, 'listening music': 1}

# 1. study 0, 1
# 2. computer 0, 1
# 3. headphone 0, 1
# 4. play basketball 0, 1
# 5. screen 0, 1
# 6. assignments: 0, 1
# 7. attend meeting 0, 1
# 8. listening music 0, 1
# 9 .reading paper 0, 1
# 10 .play computer games 0. 1
# 11. stream 0, 1
# 12. anime 0, 1
# 13. working day 0, 1, 2, 3, 4, 5, 6, 7
# 14. friends 0 ~ 49 ( intergers )
# 15. top conference : 0, 1, 2
# 16. beverage 0 ~ 2 (real number)
# 17. meal 1 ~ 5 ( intergers )
# 18. weight 50 ~ 99
# 19. shape 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 20. height 150 ~ 189

def create_student():
    student = []
    for i in range(20):
        tmp = np.random.rand()
        if i < 12 :
            if np.floor(2 * tmp) == 1:
                student.append(1)
            else:
                student.append(0)
        elif i == 12 :
            student.append(np.floor(8 * tmp))
        elif i == 13 :
            student.append(np.floor(50 * tmp))
        elif i == 14 :
            student.append(np.floor(3 * tmp))
        elif i == 15 :
            student.append(round(2 * tmp, 2))
        elif i == 16 :
            student.append(np.floor(5 * tmp) + 1)
        elif i == 17 :
            student.append(np.floor(50 * tmp) + 50)
        elif i == 18 :
            student.append(np.floor(10 * tmp) + 1)
        else :
            student.append(round((40 * tmp),2) + 150)
    return student

def classify_student(students):
    students_type = []
    for student in students:
        good_student = 20
        for itr in range(len(student)):
            if itr < 2 :
                if(student[itr]) != 1:
                    good_student = False
                    break
            elif itr == 9 :
                if(student[itr]) != 1:
                    good_student = False
                    break
            elif itr == 12 :
                if(student[itr]) < 6 :
                    good_student = False
            elif itr == 14 :
                if(student[itr]) < 1 :
                    good_student = False
            elif itr == 16 :
                if(student[itr]) > 3 :
                    good_student = False
            elif itr == 18 :
                if(student[itr]) < 5 :
                    good_student = False
        if good_student :
            students_type.append(1)
        else:
            students_type.append(0)
    return students_type

        
if __name__ == '__main__':
    np.random.seed()
    #print(create_student())
    student_list = []
    for i in range(10000):
        student_list.append(create_student())
    student_type = classify_student(student_list)
    for itr in range(len(student_type)):
        if student_type[itr] == 1:
            print(student_list[itr])