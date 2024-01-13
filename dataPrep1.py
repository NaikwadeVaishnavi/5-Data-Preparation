# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:34:11 2023

@author: DELL5300 2IN -1
"""

import pandas as pd
#*******************************


# 1 Type casting 
#import dataset
df=pd.read_csv("C:/2-dataset/ethnic diversity.csv")

#data types
df.dtypes

#salaries data types is float let us convert into int
#df1=df.Salaries.astype(int)

df.Salaries = df.Salaries.astype(int)
df.dtypes

#now the data types of salaries is int
#similarly  age data type must be float presently it is int

df.age = df.age.astype(float)
df.dtypes 


#************************************


#identify the duplicate

df_new = pd.read_csv('C:/2-dataset/education.csv')
duplicate = df_new.duplicated()
#here new series will be created after verifying

'''
output of the function is single column 
if there is duplicate record output is True 
if there is no duplicate recprd output is False
Series will be created
'''

duplicate
sum(duplicate)
#output will be 0


df_new1 = pd.read_csv('C:/2-dataset/mtcars_dup.csv')
duplicate1 = df_new1.duplicated()
sum(duplicate1)
#output will be 3 cause there are 3 duplicate values are present
#row 17 is duplicate of row 2 like wise u can 3 duplicate


#********************************#

#outlier treatement

import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/2-dataset/ethnic diversity.csv")

#now let 

sns.boxplot(df.Salaries)
#there are outlier for the salaries

sns.boxplot(df.age)
#there are no outlier

#let us calculate IQR
IQR = df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)

'''
have observed IQR in variable exploere 
no, becoz IQR is in CAPITAL letter
treated as constant
'''
IQR

'''
but if we will try as I, Iqr or iqr it is showing 

I = df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)
Iqr = df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)
iqr = df.Salaries.quantile(0.75) - df.Salaries.quantile(0.25)
'''

lower_limit = df.Salaries.quantile(0.25) - 1.5 * IQR
upper_limit = df.Salaries.quantile(0.25) + 1.5 * IQR

'''
now if u will checkthe lower limit of salary it is -19446.9675
there is negative value make it 0

how to make it
go to variable explorer and make it 0
'''

#****************************

#Trimming 

import numpy as np
'''
follownig line is to remove outlier
values which are greater than upper limit and 
lower than lower limit are removed here
'''
outliers_df = np.where(df.Salaries > upper_limit, True , np.where(df.Salaries < lower_limit ,True, False))
# u can check outliers_df column in variable explorer
df_trimmed = df.loc[~outliers_df]
df.shape
# (310, 13)
df_trimmed.shape
#(288, 13)


#***********************************

#Replacement technique

#drawback of trimming is we are losing the data
df=pd.read_csv("C:/2-dataset/ethnic diversity.csv")
df.describe

#record no 23 has got outlier
#map all the outlier value to upper limit

df_replaced = pd.DataFrame(np.where(df.Salaries > upper_limit, upper_limit, np.where(df.Salaries < lower_limit ,lower_limit , df.Salaries)))

'''
if the value are greater than upper limit
map it to upper limit and less than lower limit
map it to lower limit if it is within the range
then kept as it is
'''

sns.boxplot(df_replaced[0])

#***********************


#Winsorization (Rounding up)

from feature_engine.outliers import Winsorizer

winsor = Winsorizer(capping_method = 'iqr' , tail = 'both' , fold=1.5, variables='Salaries')

'''
copy winsorizer and paste in the help tab of 
top right window study the method
'''

df_t = winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])
