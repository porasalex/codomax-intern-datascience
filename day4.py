################## PANDAS ###############333

import pandas as pd
marks=pd.Series([10,20,30,40,50])
print(marks) 
#### tuple
page=pd.Series((43,53,63,73))
print(page)
########3 numpy array 
import numpy as np
arr=np.array([1,2,3,4,5,6])
a=pd.Series(arr)
print(a)

########### DATAFRAME #######
stu={"name":["poras","alex","puru","potter"],
     "age":[20,30,22,18],
     "marks":[100,90,80,97]
     }
df=pd.DataFrame(stu)
print(df)
###### CSV files
df1=pd.read_csv("student.csv")
print(df1)
df2=pd.read_csv("titanic.csv")
print(df2.head())# default it gives 5 heads
print(df2.head(7))
####
print(df2.tail())
print(df2.tail(7))
####
df2.info()
#gives info of dataset or file 
###
print(df2.describe())# gives numerical columns  count,avg,min,max,mean etc
###
print(df2.columns)
print(df2.isnull().sum().idxmax())#column name with the mot missing values
print(df2.isnull().sum()) #sum of all missing values in rows 
print(df2.isnull().sum().max())
#############
print(df2["Name"])#single column
print(df2[["Name","Age"]])#multiple columns
print(df2.loc[0])# select a row
print(df2.loc[0:4,["Name","Age"]])# both rows + columns
#### loc uses labels/index
# iloc uses integer positions
print(df2.iloc[0:3,0:2])# first 3 rows + first 2 columns
############ complete ##########
