#ticket price calculator_calculating ticket price based on age and contry
name = input("entre your name ")
age = int(input("enter age"))
the_price = 100
country = input("enter your country").lower()
if age >= 65 :
    print(f"hy {name} the cource is free for you")
elif age <= 12 and country != "marocco" :
    print(f"hy {name}you have a promo 30% the course price is MAD{the_price - 30} ")
elif age <= 12 and country == "marocco" :
    print(f"hy {name} you have a promo 50% the course price is MAD{the_price - 50}")
else :
    print(f"hy {name} the course price is MAD{the_price} ")










