from ast import Add


print("Hello World!")

#string
# name = input("Enter any name: ")
# print(name)

#addition
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# sum = num1 + num2
# print(sum)

#eg
# num1 = int(input("Enter a number: "))
# if num1>0:
#    print("this is positive")
# elif num1<0 :
#    print("this is negative")
# else:
#     print("this is zero")
    
#greater
# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter num2: "))
# if num1>num2 :
#     print(f"{num1} is greater than {num2}") #f helps to print number instead of text
# else :
#     print(f"{num2} is greater than {num1}")    

#Assignment
#Write a program in python to find the greatest among three.
# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))
# if (num1 >= num2) and (num1 >= num3):
#    print(f"{num1} is greatest")  
# elif (num2 >=  num1) and (num2 >= num3):
#    print(f"{num2} is greatest")
# else:
#    print(f"{num3} is greatest")       
   
   
#Take a inputs from the users which shoulld be divisible by 3 ,if dividible by 5,if divisible by 7
num = int(input("Enter a number: ")) 
if  num % 3 == 0 and num % 5 == 0 and num % 7 == 0 :
     print(f"{num} is divivible by 3,5,7")
elif num % 3 == 0 and num % 5 == 0 :
    print(f"{num} is divisible by 3,5")     
elif num % 3 == 0 and num % 7 == 0 :
    print(f"{num} is divisible by 3,7") 
elif num % 5 == 0 and num % 7 ==0 :
    print(f"{num} is divisible by 5,7")
elif num % 3 == 0 :
    print(f"{num} is divisible by 3")
elif num % 5 == 0 :
    print(f"{num} is divisible by 5") 
elif num % 7 == 0 :
    print(f"{num} is divisible by 7") 
else :
    print(f"{num} is not divisible")       