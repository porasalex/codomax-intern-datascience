########## improvising 
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned_titanic.csv")

print("========= titanic dataset analysis ============")
#creating the dashboard
plt.figure(figsize=(6,4))

#barchart
#shows survival distribution
df["Survived"].value_counts().plot(kind="bar",color=["skyblue","orange"])
plt.title("survival count")
plt.xlabel("survived/not survived")
plt.ylabel("no.of people")
plt.tight_layout()
plt.show()

#histogram
#shows age distribution
plt.figure(figsize=(6,4))
plt.hist(df["Age"],bins=20)
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequecy")
plt.tight_layout()
plt.show()