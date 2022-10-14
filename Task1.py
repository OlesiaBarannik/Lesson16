from datetime import date

class Person:
    def __init__(self, last_name, first_name, date_of_birth):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth

    def fullname(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


class Student(Person):
    def __init__(self, last_name, first_name, date_of_birth, scholarship, age):
        super().__init__(last_name, first_name, date_of_birth)
        self.scholarship = scholarship
        self.age = age


class Teacher(Person):
    def __init__(self, last_name, first_name, salary, subject, date_of_birth):
        super().__init__(last_name, first_name, date_of_birth)
        self.salary = salary
        self.age = subject

    def get_salary(self):
        return self.salary

    def change_salary(self, new_salary):
        self.salary = new_salary



st = Student("Evelina", "Sarkisian", date_of_birth =  date(1997, 2, 3), scholarship = 5000, age = 6)
print(st.first_name)
print(st.last_name)
print(st.scholarship)
print(st.fullname())
print(st.get_age())

teach = Teacher("Barannik", "Olesia", salary = 20000, subject = "history", date_of_birth = date(1983, 2, 3))
print(teach.fullname())
print(teach.get_salary())
teach.change_salary(30000)
print(teach.get_salary())
print(teach.get_age())

