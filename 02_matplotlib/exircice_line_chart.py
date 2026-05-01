# Basic Bar and Line Charts
# Visualizing employees salary data with matplotlib

import pandas as pd 
import matplotlib.pyplot as plt

data = {
    "name": ("amine", "solaimane", "med", "samia"),
    "salary": (12000, 50000, 3000, 1500)
}
df = pd.DataFrame(data)
print(df)
#visualizing employees salary with matplotlib bar chart
plt.bar(df["name"], df["salary"])
plt.title("bar chart")
plt.xlabel("employees name")
plt.ylabel("employees salry")
plt.show()

#visualizing employees salary with line chart 
plt.plot(df["name"], df["salary"])
plt.title("line chart")
plt.xlabel("employees name")
plt.ylabel("employees salary")
plt.show()








