# class Student:
#     def __init__(self, _id, name, rollno):
#         self._id = _id
#         self.name = name
#         self.rollno = rollno
#         self.total_attendence = 0
#     def view_attendance(self):
#         print(f"Total attendence of {self.name} = {self.total_attendence}")
#     def __str__(self):
#         return f"{self.rollno}. {self.name}"
#     def __repr__(self): 
#         return f"{self.rollno}. {self.name}"
              
       
# s = Student(1, "Ram", 1)
# s.view_attendance
# s2 = Student(1, "sahym", 1)
# s2.view_attendance

# students = []
# for i in range(1,4):
#     name = input("Enter name: ")
#     rollno = input("Enter roll no: ")
#     s = Student(i,name,rollno)
#     students.append(s)
# print(students)    


#INHERITENCE
# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
    
#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
       

# class Student(Person):
#     def __init__(self, name, address, roll_number):
#         super().__init__(name, address)
#         self.roll_number = roll_number
    
#     def profile(self):
#         super().profile()
#         print(f"Roll number: {self.roll_number}") 
    
# class Staff(Person):
#     def __init__(self, name, address, designation):
#         super().__init__(name, address)
#         self.designation = designation

# s = Student("Ram","Ktm",1)
# s.profile()


