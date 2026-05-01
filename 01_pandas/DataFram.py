#stor_sales_analysis.py 
import pandas as pd 
data = {
    "product": ("phone", "tv", "computer"),
    "quantity": (5000, 1000, 3000),
    "prix": (1000, 3000, 2000)
}
df = pd.DataFrame(data)
#add total column 
df["total"] = df["quantity"] * df["prix"]
print(df["total"])
#total sales 
print(df["total"].sum())
#the most expencive product
print(df.loc[df["prix"].idxmax(), "product"])
#total > 5000 
print(df[df["total"] > 5000 ])







