#  GLOBAL AND LOCAL SCOPE
# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     inner()
        
# outer()  

#NEW
# def welcome():
#     print("welcome everyone!")
    
# print(f"Welcome: {welcome}")
# a = welcome
# print(f"a: {a}")
# a()

# def product(num1,num2):
#    return num1 * num2

# p = product
# print(p(10,2))



#higher order function
#decorator

#SEVENTH CLASS

# def welcome(name):
#    print(f"Welcome {name}!")
   
# def bye(name):
#    print(f"Bye Bye {name}!")   
   
# def greet_person(func):
#    func("Ram")        
   
# greet_person(welcome)
# greet_person(bye)


#
# def outer():
#    #  print("I am outer function")
#    def inner():
#         print("I am inner function")
#    return inner

# i = outer()
# i()

#CLOSURE

# def increment(num):
#    def increase_by(factor):
#       return num + factor
#    return increase_by

# inc = increment(20)
# print(inc(50))   


#HIGHER ORDER FUNCTION
#DECORATOR

# def decorator_function(func):
#    def wrapper():
#       print("I am called before function")
#       func()
#       print("I am called after example")
#    return wrapper   

# @decorator_function
# def example():
#    print("I am example")
   
   
# example()   


#decorator

# def smart_division(func):
#    def wrapper(a,b):
#       if b == 0 :
#          return "Cannot be divided"
#       else:
#          return func(a,b)
#    return wrapper   

# @smart_division
# def division(a,b):
#    return a / b

# print(division(10,2))
# print(division(10,0))


#BUILT-IN HIGHER ORDER FUNCTION
#MAP FUNCTION

#lambda
# a = lambda x , y : x + y
# print(a(10,5))

#MAP - can pass function and iterable_object
# a = [1,2,3,4,5]
# # b[]
# # for i in a:
# #    b.append(i+1)
# # def incre(n):
# #    return n+1   
# out = map(lambda n:n+1,a)
# print(list(out))
   
   
#FILTER-can pass function and iterable_object sets value only true
# a = [1,2,3,4,5,6,7,8,9]
# out = filter(lambda n : n % 3 ==0 , a)
# print(list(out))

# student_marks = [
#    {"name":"Ram","score":80},
#    {"name":"Sita","score":75},
#    {"name":"Shyam","score":40},
#    {"name":"Avay","score":35},
#    {"name":"samy","score":31},
#    {"name":"Rita","score":65},
      
# ]


# marks = filter(lambda i:i.get("score") >= 40,student_marks)
# print(list(marks))


#Assignment
# main = []
# even = []
# odd = []
# duplicate = []

# #take user input 15 times in int
# #append all user input in main list
# #append even number in even list
# #append odd number in odd list
# #append duplicate entry into duplicate list


# for i in range(15):
#    num = int(input("enter a number: "))
#    if num in main:
#       duplicate.append(num)
      
#    else:
#       if num % 2 == 0 :
#          even.append(num)
#       else:
#          odd.append(num)
        
#    main.append(num)
   
# print("Main: ",main)   
# print("Even number:" ,even)
# print("Odd number:", odd)
# print("Duplicate: ", duplicate)
   
   


# colors = ["yellow","green","red","blue","yellow","red"]
# to_be_removed = ["yellow" ,"red"]
# new_colors = []

# # for color in colors:
# #    if color not in to_be_removed:
# #       new_colors.append(color)
      
# # print(new_colors)    

# print(list(filter(lambda color:color not in to_be_removed,colors)))  


# a = "876d59e45"
# total = 0

# for i in a:
#    if i.isdigit():
#        total = total + int(i)
      
# print(total)

#ALTERNATIVE

# output = filter(str.isdigit,a)
# o = map(int,output)
# print(sum(0))














