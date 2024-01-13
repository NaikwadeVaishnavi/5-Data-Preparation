# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:28:24 2023

@author: vaish
"""    

import pandas as pd

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()

#we use ethnic diversity dataset

df=pd.read_csv('C:/2-dataset/ethnic diversity.csv')
df.columns

'''
we have salaries and age as numerical columns let us make 
them at position 0 and 1 to make fuether data processing easy
'''

df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus', 'Department', 'Race']]

'''
check the dataframe in variable explorer we want only nominal data &
ordinal data for processing hence skippped 0th and final column
and applied to one hot encoder
'''

enc_df = pd.DataFrame(enc.fit_transform(df.iloc[:,2:] ).toarray())
#drawback of the encoding df =in tranform dataframe columns dont have names so we have to rename them 

#*********************

from sklearn.preprocessing import LabelEncoder
#creating instance of the lable encoder

labelencoder = LabelEncoder()
#split your data into input and output variables

x = df.iloc[:,0:9] #first eight columns for x and 9th for y or 1
y = df['Race']
df.columns

'''
we have nominal data sex MaritalDesc CitizenDesc
we want to convert to label encoder
'''

x['Sex'] = labelencoder.fit_transform(x['Sex'])
x['MaritalDesc'] = labelencoder.fit_transform(x['MaritalDesc'])
x['CitizenDesc'] = labelencoder.fit_transform(x['CitizenDesc'])

#label encoder y

y =  labelencoder.fit_transform(y)

'''
This is going to create an array hence convert it back to dataframe
'''

y = pd.DataFrame(y)
df_new = pd.concat([x,y],axis=1)

'''
if u will see  variable explorer y do not have column name 
hence remove the column 
'''

df_new = df_new.rename(columns = {0:'Race'})
#previously df_new has column name 0 it will be renamed 
