# Job Market Analysis Dashboard  
# Analyzing and visualizing real job market data
import pandas as pd 
import matplotlib.pyplot as plt 
data = {
   "job": ("Data Analyst", "Developer", "Designer", "HR Manager", 
           "Data Analyst", "Developer", "Accountant", "HR Manager"),
   "salary": (12000, 10000, 8000, 7000, 11000, 9000, 6000, 7500),
   "sector": ("Tech", "Tech", "Tech", "RH", "Tech", "Tech", "Finance", "RH"),
   "city": ("Casablanca", "Rabat", "Casablanca", "Fes", 
            "Rabat", "Casablanca", "Fes", "Rabat"),
   "experience": (3, 2, 1, 5, 4, 2, 3, 3),
   "contract": ("CDI", "CDI", "CDD", "CDI", "CDD", "CDI", "CDD", "CDI")
}

df = pd.DataFrame(data)
#calcule the average salary for each sector
average_salary_by_sector = df.groupby["sector"]("salary").mean()
#calcule the number of job for each type of contract
df.groupby("contract")["job"].count() 
#subplot 
plt.subplot(2, 2, 1)
plt.bar(average_salary_by_sector.index, average_salary_by_sector.values)
plt.title("bar chart")
#pie chart 
plt.subplot(2, 2, 2)
plt.pie(df["contract"].value_counts(), labels=df["contract"].value_counts().index, autopct="%1.1f%%")
plt.show()
#scateer plot
plt.subplot(2, 2, 3)
plt.scatter(df["experience"], df["salary"])
#bar chart for the number of job for each city and bar chart
job_by_city = df.groupby("city")["salary"].sum()
plt.subplot(2, 2, 4)
plt.bar(job_by_city.index, job_by_city.values)

plt.show()








