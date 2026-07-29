####### DASHBOARD ############
import pandas as pd
import matplotlib.pyplot as plt
#read dataset
df=pd.read_csv("titanic.csv")

#creating theb dashboard
plt.figure(figsize=(12,8))

#barchart
plt.subplot(2,2,1)
df["Survived"].value_counts().plot(kind="bar")
plt.title("survival count")

#piechart
plt.subplot(2,2,2)
df["Sex"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("gender distribuion")

#histogram
plt.subplot(2,2,3)
df["Age"].plot(kind="hist",bins=10)
plt.title("Age distribution")

#boxplot
plt.subplot(2,2,4)
df["Fare"].plot(kind="box")
plt.title("Fare dstribution")

## showing dashboard
plt.suptitle("Titanic dataset dashboard")
plt.tight_layout()
plt.show()
