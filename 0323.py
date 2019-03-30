c={
    1:[65,50,'male'],
    2:[80,80,'male'],
    3:[72,91,'female']
}
def add(c,id,grade_1,grade_2,gender):
    c[id]=[grade_1,grade_2,gender]

def delete(c,id):
    del c[id]

def print_all(c):
    for id in c:
        print('ID',id,"---",'literature grade:',c[id][0],', math grade:',c[id][1],', gender:',c[id][2])


def print_one(c,id):
    print('ID',id,"---",'literature grade:',c[id][0],',math grade:',c[id][1],',gender:',c[id][2])

print('1 means add a student\n2 means delete a student\n3 means print the students list\n4 means print one student\n5 means break the program')
while True:
    choice=input('please enter your choice: ')
    if choice=='1':
        id=int(input('please enter the id: '))
        lg=int(input('enter literature grade: '))
        mg=int(input('give me math grade: '))
        gender=input('tell me the gender: ')
        add(c,id,lg,mg,gender)
        print('excuted')
    elif choice=='2':
        people=int(input('who do you want to delete: '))
        delete(c,people)
        print('excuted')
    elif choice=='3':
        print_all(c)
    elif choice=='4':
        people_choice=int(input('who do you want to print: '))
        print_one(c,people_choice)
    elif choice=='5':
        print('program breaked')
        exit()
    else:
        print("invalid input\n-------------------------------------------------------")
        print('1 means add a student\n2 means delete a student\n3 means print the students list\n4 means print one student\n5 means break the program')

