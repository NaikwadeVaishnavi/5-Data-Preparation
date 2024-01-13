# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:20:41 2023

@author: vaish
"""
#*******************
#STANDARDISATION

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

d = pd.read_csv('C:/2-dataset/mtcars.csv.xls')
a = d.describe()

#intialize the  scalar

scalar = StandardScaler()
df = scalar.fit_transform(d)
dataset = pd.DataFrame(df)
res = dataset.describe()

'''
here if you will check res in variable explorer environmental then
 '''
 
d = pd.read_csv('C:/2-dataset/Seeds_data.csv.xls')
a = d.describe()

#intialize the  scalar

scalar = StandardScaler()
df = scalar.fit_transform(d)
dataset = pd.DataFrame(df)
res = dataset.describe()

#********************
#NORMALIZATION

ethnic = pd.read_csv("C:/2-dataset/ethnic diversity.csv")
#now read columns

ethnic.columns
#there  are some columns which are not useful that we need to drop 

ethnic.drop(['Employee_Name', 'EmpID', 'Zip'],axis=1,inplace=True)

#now read the min and max value of salaries and the age

a1=ethnic.describe()
a1

'''
check a1 data from variable explorer 
u will find min salary is 0 and max salary is 108304
samw way check for the age there is huge difference 
in min and max value 
hence we are going for the normalization
first we will have to convert non-numeric data to label encoding
'''

ethnic = pd.get_dummies(ethnic,drop_first=True)

#normalization function written where ethnic argument is passed

def norm_func(i):
    x = (i-i.min()) / (i.max()-i.min())
    return x
df_norm = norm_func(ethnic)

b=df_norm.describe()
b

'''
if you will observe the b frame 
it has dimension 8,81
earlier in a they were 8,11
it is because all non-numeric 
data has been converted to numeric using label conding
'''