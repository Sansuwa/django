# FUNCTION 
#FIFTH CLASS

# def function_name():
#     #function body
     
# #function_name: funcion signature


# def func_name():
#     print("hello,I'm a function")
    
# # func_name() -> function execution
# func_name  -> function reference 


#SIXTH CLASS

# def profile(name,contact,address):  #fun with parameter
#     print(f"Name:{name}")
#     print(f"Contact:{contact}")
#     print(f"Address:{address}")
    
# #positional arguments
# profile("Ram","9876","ktm")    #arguments


# #keyword arguments
# profile(name="Ham",address="ktm",contact="9876")  

#default argument
# def exponent(base, power=1):
#     print(base**power)

# exponent(5)
 
#alt
# def exponent(base, power):
#     print(base**power)

# exponent(5,2)

#function without return type and with retur type

# def addition(num1, num2):
#     print(num1 + num2)
    
# def product(num1, num2):
#     return(num1 * num2) 
 
    
# res = addition(2,5)
# print(f"Addition: {res}")  
# ans = product(10,2)
# print(f"Product: {ans}") 


# * gives tuple 
# def example(*a):
#     for i in a:
#         print(i) 
        
# example(1,2,3,4,5)    

# ** gives dict        
# def example(**a):
#     print(a)
    
# example(name="Ram",address="ktm",contact="9876")   

def profile(name,contact,address): 
    print(f"Name:{name}")
    print(f"Contact:{contact}")
    print(f"Address:{address}")
    
a = {"name":"Ram","address":"ktm","contact":"9876"}
profile(**a)

