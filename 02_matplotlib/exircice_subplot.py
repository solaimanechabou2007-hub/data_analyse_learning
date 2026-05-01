# Pie Chart and Subplots
# Visualizing sales data with multiple chart types
import pandas as pd 
import matplotlib.pyplot  as plt 

data = {
    "product": ("phone", "tv", "computer"),
    "prix": (2000, 4000, 3000),
    "sales": (200, 300, 200)
}
df = pd.DataFrame(data)
#visualizing the most popular product
print(df.loc[df["sales"].idxmax(), "product"])
print(df)
#pie chart for sales product
plt.subplot(1, 2, 1)
plt.pie(df["sales"], labels=df["product"])
plt.title("pie chart")
#bar chart for 
plt.subplot(1, 2, 2)
plt.bar(df["product"], df["prix"])
plt.title("bar chart")
#show all 
plt.show()










