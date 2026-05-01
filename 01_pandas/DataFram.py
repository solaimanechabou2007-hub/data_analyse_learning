# Employees DataFrame Basics
# Creating and filtering a DataFrame of employees
import pandas as pd 
data = {
    "name":("solaimane", "amine", "samia", "mohamed", "aya"),
    "salary": (5000, 4000, 3000, 1200, 5700),
    "city": ("mknes", "imlchil", "marakech", "marakech", "imilchil")
    }
df = pd.DataFrame(data)
print(df)
print(df.describe())
#employees frome imilchil
print(df[df["city"] == "imilchil"])
#employees with salary >4000
print(df[df["salary"] > 4000 ])













