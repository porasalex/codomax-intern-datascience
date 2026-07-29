################## DATA FILTERING ################
import pandas as pd
df=pd.read_csv("titanic.csv")
print(df.head())
#taking first 5 (default)rows with head()
print(df["Name"])
# selecting one column
print(df[["Name","Age","Sex"]])
#selecting multiple columns
# for multiple columns use two square brackets ,passing a list 

#### filtering rows

# showing only the passengers whose age is above 30
print(df[df["Age"]>30])    # boolean indexing
#df=df[age]>30
#if age >30 true keep the row, false remove the row

#### filtering with two conditions
#passengers olderthan 30 and female
print(df[(df["Age"]>30)&(df["Sex"]=="female")])
# & AND both true

#pasengers olderthan 60 or younger than 10
print(df[(df["Age"]>60)|(df["Age"]<10)])
#only one must be true

#sorting by age
print(df.sort_values("Age")) # ascending order
print(df.sort_values("Age",ascending=False)) # descending order
# it also works ascending=True
