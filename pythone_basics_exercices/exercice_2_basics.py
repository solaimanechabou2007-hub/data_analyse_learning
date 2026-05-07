#grad calculator_calculating student result and mention
name = input("enter your name ")
notes = int(input("enter your note"))

if notes >= 16 :
    print(f"hello {name}your mention is exellent")
elif notes < 16 and notes >= 15 :
    print(f"hello {name} your montion is trés bien ")
elif notes <= 14 and notes >= 12 :
    print(f"hello {name} your mention is bien")
elif notes < 12 and notes >= 10 : 
    print(f"hello {name} your mention is passble")
else:
    print(f"{name} you failed")












