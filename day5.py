######### CHECKING MISSING VALUES ###########
import pandas as pd
df=pd.read_csv("titanic.csv")
print(df.isnull().sum())
#isnull() is for missing values
#sum() is for count no.of missing values 

######## REMOVE MISSING VALUES ########
df_clean=df.dropna()
print(df_clean)
# dropna() removes rows containg the missing  values

###### FILL MISSING VALUES ##########
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df["Age"])
# missing places getting replaces with mean value
# omly for numerical colunms ,uses mean 

############ FIND DUPLICATE VALUES ###########
print(df.duplicated().sum())
# duplicated() marks duplicate rows
# sum()counts them

######## REMOVE DUPLICATE VALUES #####
df=df.drop_duplicates()
print(df.shape)
# drop_duplicate() removes the repeated rows
# shape tells (rows, colunms)

############ RENAME COLUNMS #############
df=df.rename(columns={"sex":"gender"})
print(df.columns)
# df.rename the sex column name with gender
#only the sex column name chages 

########## CHANGE DATA TYPE ############3
print(df["Age"].dtype)
df["Age"]=df["Age"].astype(int)
print(df["Age"].dtype)
# astype() converts the datatype of column
#float64 becoms int64
###### it only works when there are no null values in the column
# with nan values it raises errror
