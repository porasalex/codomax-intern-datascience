################# EXPORTING CLEANED DATASET ##########
import pandas as pd
df=pd.read_csv("titanic.csv")# reading file
df.head()#looking for a view 
df.isnull().sum()#missing values values in each column
df.duplicated().sum()# shows how many duplicate rows exist
df["Age"]=df["Age"].fillna(df["Age"].mean())#replacing missing age places with avg age
df.drop_duplicates(inplace=True)# remove duplicate rows
#inplace=true means edit on same dataframe
# verifying
print(df.isnull().sum())

### cleaning remaining 
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
#using mode() since it doesnot contain numerical values
df.drop(columns=["Cabin"],inplace=True)
#since cabin column contains more than half missing values so we drop it for data quality
print(df.isnull().sum())
print(df.duplicated().sum())
df.to_csv("cleaned_titanic.csv",index=False)

