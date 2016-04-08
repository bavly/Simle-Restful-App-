

from statistics import mean as m

#from lib import statistics

Admins = {'bavly': 'bav0123','andro':'zero'}
studentDict = {'jeff':[81,91,52],
               'Alex':[14,25,55],
               'Sam':[87,54,56]}

def enterGrades():
    name = input('Student name : ')
    grade = input('Grade : ')
    if name in studentDict:
        print ('adding student ....')
        studentDict[name].append(float(grade))
    else:
        print ('Student does not exist ')

    print (studentDict)

def removeStudent():
    nametoremove = input('what student do you want to remove ?')
    if nametoremove in studentDict:
        print ('removing student')
        del studentDict[nametoremove]

    print (studentDict)


def StudentAverage():
    for eachstudent in studentDict:
        gradelist = studentDict[eachstudent]
        avgGrade = m (gradelist)
        print (eachstudent , 'has an average grade of :', gradelist)

def main():


    print ("""
    welcome to Grade system

    [1]  -  Enter Grades
    [2]  -  Remove Student
    [3]  -  Student Average
    [4]  - Exit

    """)

    action = input('what is your chooice today ? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        StudentAverage()
    elif action == '4':
          exit()
    else:
        print ('the chooice you had enter is wrong please try again ')
       # main()
        #pass

login = input('user name : ')
password = input('password :')

if login in Admins:
    if Admins[login] == password:
        print ('welcome' , login)
        while True:
            main()
    else :
        print ('invalid password' )
else :
    print ('invalid user name' )


