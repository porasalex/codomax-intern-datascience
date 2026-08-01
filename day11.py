################### FINDING BUSINESS INSIGHTS########
################# DAY 11 
############
########
import pandas as pd
df=pd.read_csv("cleaned_titanic.csv")
print("INSIGHTS FROM THE CLEANED TITANIC DATASET")
print(df["Survived"].value_counts())
#this shows how many people survived and not survived
print("1. more passengers died than survival(549 vs 342)")
print(df.groupby("Sex")["Survived"].mean()*100)
#this shows who had more survival rate male or female
print("2. female passengers have higher survival rate(74.2%) than male passengers(18.8%)  ")
print(df.groupby("Pclass")["Survived"].mean())
#this shows which class passengers survived more 
print("first class has the highest surivival rate than second class and third class() ")
print(df["Embarked"].value_counts())
#this shows the port that is most common
print("most passengers are boarded from S (southampton)")
print(df["Fare"].describe())
# this shows the all details of the Fare prizes
print("fare prizes mean was 32.0 while the highest was 512.33 which shows few passengers paid very high fares")
