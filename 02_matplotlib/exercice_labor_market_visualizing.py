# Labour Market Visualization
# Analyzing and visualizing job market data
import pandas as pd 
import matplotlib.pyplot as plt

data = {
    "name": ("solaimane", "amine", "aya", "med", "samia"),
    "salary": (20000, 10000, 4000, 7000, 3000),
    "city": ("mknes", "imilchil", "imilchil", "mrakech", "mrakech"),
    "sector": ("marketing", "tech", "education", "finance", "RH"),
    "experience": (10, 6, 5, 8, 6)
}
df = pd.DataFrame(data)
#bar chart for an average salary in each sector
average_by_sector= df.groupby("sector")["salary"].mean()
plt.subplot(1, 3, 1)
plt.bar(average_by_sector.index, average_by_sector.values )
plt.title("bar chart")
#pie chart for the number of sectors in each city
plt.subplot(1, 3, 2)
plt.pie(df["city"].value_counts())
plt.title("pie chart")
#scatter plot for the relation between salary and sector
plt.subplot(1, 3, 3)
plt.scatter(df["experience"], df["salary"])
plt.title("scatter plot")
plt.show()





























