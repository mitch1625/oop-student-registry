class Student:
    def __init__(self, name:str, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self):
        return f'Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}'        
    
    @property
    def get_name(self):
        return self._name
    
    @property 
    def get_age(self):
        return self._age
    
    @property
    def get_grade(self):
        return self._grade
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.isalpha():
            self._name = new_name
        else:
            print('Invalid Name')

    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 11 and new_age < 18:
            self._age = new_age

    @get_grade.setter
    def set_grade(self, new_grade):
        if isinstance(new_grade, str) and new_grade == "9th" or new_grade == "10th" or new_grade == "11th" or new_grade == "12th":
            self._grade = new_grade

    def study(self, subject):
        print(f'{self._name} is studying {subject}')

    def advance(self): 
        grade = self._grade
        grade = str(int(grade[:-2])+1) + "th"
        print(f'{self._name} has advanced to {grade} grade')



list = [1,2,3,4,5]
for elem in list:
    if (elem[i] > 0):
        print(elem)