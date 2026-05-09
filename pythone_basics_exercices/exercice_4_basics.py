#job aplication checker-checking if candidat meets job requirements
name = input("enter your name ")
age = int(input("enter your age  "))
yers_of_experience = int(input("enter yers of experience "))
city = input("enter your city ")
grad = input("enter your grad ")
age_ok = 22 <= age <= 45
if  age_ok and yers_of_experience >= 2 and grad in ["master", "licence"] and city in ["rabat", "casablanca"] :
    print(f"congratulation {name} you are accepted")
else: 
    print(f"sorry{name} you dont meet the requirements")












