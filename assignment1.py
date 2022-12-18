#Assignment
# [1] Write a program in python to find the greatest among three.
# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))
# if (num1 >= num2) and (num1 >= num3):
#    print(f"{num1} is greatest")  
# elif (num2 >=  num1) and (num2 >= num3):
#    print(f"{num2} is greatest")
# else:
#    print(f"{num3} is greatest")       
   
   
# [2] Take a inputs from the users which shoulld be divisible by 3 ,if dividible by 5,if divisible by 7
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