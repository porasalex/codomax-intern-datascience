############### DATA VISUALIZATION #############
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("titanic.csv")
survival=df["Survived"].value_counts()
print(survival)
# value_counts() counts frequency of each unique value
#count() counts non missing values
######## bar graph #########
survival.plot(kind="bar")
plt.title("survived vs not survived ")
plt.xlabel("survival")
plt.ylabel("no.of passengers")
plt.show()

########## PIE CHART #########
df["Survived"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("Survival percentage")
plt.show()
### autopct is for percetages

######## HISTOGRAM ##########3
df["Age"].plot(kind="hist",bins=10)
#bin=10 divides graphs into 10 parts
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("frequency")
plt.show()

########## BOXPLOT ############
df["Fare"].plot(kind="box")
plt.title("fare box plot")
plt.show()

################ LINE CHART ##############
df["Fare"].head(20).plot(kind="line")
plt.title("Fare line chart")
plt.xlabel("passenger")
plt.ylabel("Fare")
plt.show()



