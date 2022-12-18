#WHILE LOOP
# while True;
#      print("i am inside loop")
     
#eg
# a = 1
# while a <= 10:
#     print(f"{a} times")
#     a = a+1     

#take username and password as input 
#until user provide correct ones
#username: abc@gmail.com
#password: 12345


# uname = "abc@gmail.com"
# pword = "12345"
# username = input("Username: ")
# password = input("Password: ")
# while username != uname or password != pword:
#     username = input("Username: ")
#     password = input("Password: ")
# print("successful") 

# #
# a ={"name":"ram","contact":"98765","address":"ktm"}
# # print(a.keys())
# print(a.values())
# print(a.items())

# for i in a.keys():
#     print(i)

# for i in a.values():
#     print(i)
    
# for x,y in a.items():
#     print(x,y)
    
# a = {
#     "properties":{
#         "profiles":{
#             "name": "ram",
#             "education":[
#                 {"college":"ABC","year":"2018"},
#                 {"college":"XYZ","year":"2019"},
                
#             ]
#         },
#         "followers":1000,
#         "following":50,
#     }
# }

# name = a.get("properties").get("profiles").get("name")
# followers = a.get("properties").get("followers")
# following = a.get("properties").get("following")

# print(f"Name: {name}")
# print(f"followers: {followers}")
# print(f"following: {following}")

# educations = a.get("properties").get("profiles").get("education")
# for education in educations:
#     year = education.get("year")
#     college = education.get("college")
# print(f"Education({year}): {college}")


#output
# Name: ram
# followers: 1000
# following: 50
# Education(2019): XYZ



oil_prices = [
    {
        "oil_type":"petrol",
        "prices":
        [
            {"year":"2018","price":100},
            {"year":"2019","price":120},
            {"year":"2020","price":180},           
        ]
    },
    {
        "oil_type":"diesel",
        "prices":[
            {"year":"2018","price":80},
            {"year":"2019","price":100},
            {"year":"2020","price":160}, 
            
        ]
    }
       
]
    


# print("_"*25)
# summ , summ1 = 0,0
# oil_type = oil_prices[0].get("oil_type")
# year2018 = oil_prices[0].get("price")
# print("Oil Type: ",oil_type)
# for i in range(0,3):
#     print("Year(", year2018[i].get("year"),") Rs:",year2018[i].get("price"))
#     summ = int(year2018[i].get("price")) + summ


# print("_"*25)
     
# oil_type = oil_prices[1].get("oil_type")
# year2018 = oil_prices[1].get("price")
# print("Oil Type: ",oil_type)
# for i in range(0,3):
#     print("Year(", year2018[i].get("year"),") Rs:",year2018[i].get("price")) 
#     summ1 = int(year2018[i].get("price")) + summ1    


# print("_"*25)
# print("Petrol Price(2018-2020): " ,summ)
# print("Disel Price(2018-2020): " ,summ1)

print("_"*25)

for oil in oil_prices:
    print(f"Oil Type: {oil.get('oil_type').capitalize()}")
    prices = oil.get('prices')
    total = 0
    for price in prices:
       p = price.get('price')
       total = total + p
       print(f"Price: ({price.get('year')}) : {p}")
    print(f"Price(2018-2019): {total}")  
      
    #avg_price = round(total/len(price),2)
    #print(f"Average Price: {avg_price}") 

    print("_"*25)   


  



    

