################## DATA ANALYSIS ############
import pandas as pd
df=pd.read_csv("titanic.csv")
print(df["Fare"].sum())
# returns the total fare total amount that passengers paid

# avg()
print(df["Age"].mean())
#returns the avg value of all passengers age

#min()
print(df["Age"].min())
# returns the youngest passenger age

#max()
print(df["Age"].max())
print(df["Age"].idxmax()) # returns the row number of mx value
#returns the oldest person age

#count()
print(df["Age"].count())
#returns the count of all no.of non missing age values
#count() dont consider the nan values

#entire row of the person who paid the high fare prize
print(df.loc[df["Fare"].idxmax()])

