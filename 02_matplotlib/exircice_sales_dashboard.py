# Sales Dashboard
# Creating a complete sales analysis dashboard with 4 charts
import pandas as pd
import matplotlib.pyplot as plt 

data = {
   "mois": ("Jan", "Fév", "Mar", "Avr", "Mai", "Jun"),
   "ventes": (15000, 18000, 12000, 22000, 19000, 25000),
   "depenses": (8000, 9000, 7000, 11000, 10000, 12000),
   "profit": (7000, 9000, 5000, 11000, 9000, 13000)
}

df = pd.DataFrame(data)
print(df)
#line chart for the evolution of sales over time
plt.plot(df["mois"], df["ventes"], color="green", marker="o" )
plt.title("ventes mensuelles")
plt.xlabel(df["mois"])
plt.ylabel("ventes")
plt.show()
#par chart to comparer sales and expeses
plt.bar(df["ventes"], df["depenses"],  color="blue")
plt.title("depences ventes")
plt.xlabel("depenses")
plt.ylabel("ventes")
plt.show()
#pie chart for the percentage of profits every months
plt.pie(df["profit"], labels=df["mois"])
plt.title("pie chart")
plt.show()
#scateer plot for the relation between depenses and profit
plt.scatter(df["depenses"], df["profit"])
plt.title("sateer plot")
plt.show()





