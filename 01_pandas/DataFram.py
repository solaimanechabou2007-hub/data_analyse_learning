# Students GroupBy Analysis
import pandas as pd 
data = {
    "name": ("solaimane", "amine", "mohamed"),
    "note": (13, 16, 17),
    "city": ("mknes", "imilchile", "marakech",),
    "departement": ("phisique", "francis", "mathematiques")
}
df = pd.DataFrame(data)
#calculat th average score for ech city with groupby
df.groupby("city")["note"].mean
#average for any city
df["average"] = df["note"].mean()
print(df["average"]) 
#Add the results column if the point is greater than or equal to 10 it is successful
#, and if the word is less, it is a sedipitate
df["results"] = df["note"].apply(lambda x: "passé" if x >= 10 else "failed")
#print the number of succceful and repeaters
print(df[df["results"] == "passé"].shape[0])
print(df[df["results"] == "failed"].shape[0])























