# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:41:16 2023

@author: vaish
"""


import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/modified ethnic.csv.xls")

df.head(10)
#first 10 rows

df.info()
#tell the info of the data i.e number of non-null values 

df.describe()
#5 number summary only applicable for numerical var not for nominal var

df['Salaries_new']=pd.cut(df['Salaries'],bins=[min(df.Salaries),df.Salaries.mean(),max(df.Salaries)],labels=['low','high'])

df.Salaries_new.value_counts()

'''
low     147
high    130
Name: Salaries_new, dtype: int64
'''

df['Salaries_new']=pd.cut(df['Salaries'],bins=[min(df.Salaries),df.Salaries.quantile(0.25),df.Salaries.mean(),df.Salaries.quantile(0.75),max(df.Salaries)],labels=['g1','g2','g3','g4'])

df.Salaries_new.value_counts()
'''
g2    78   
g4    70
g1    69
g3    60
Name: Salaries_new, dtype: int64
'''


df=pd.read_csv('c:/2-dataset/animal_category.csv.xls')
df.shape
#(30, 5)
df.columns
df.drop(['Index'],axis=1,inplace=True)
#check  the df again

df_new=pd.get_dummies(df)
#gives dummy data in terms of 0 & 1

df_new.shape
#(30, 14)

'''
here we are getting 30 rows and 14 columns
we are getting two columns for homely and gender one column
delete second columns of gender and second column  of homely
'''

df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape
#(30, 12)

df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'Homly'},inplace=True)


#******************
df1=pd.read_csv('c:/2-dataset/ethnic diversity.csv')
df1.shape
df1.columns
