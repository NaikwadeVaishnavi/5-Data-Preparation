# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:29:27 2023

@author: vaish
"""

'''
zero varience and near zero varience 
if there is no varience in the figure then it is better 
to ignore feature
'''
import pandas as pd

df=pd.read_csv('C:/2-dataset/ethnic diversity.csv')
df.var()

'''
here EmpId and Zip is nominal data 
salary has  4.441953e+08  is 444195300 which is not close to 0
similary for age 
both feature are having considerable varience
'''

df.var(axis=0)==0 #check varience of the row data

df.var(axis=1)==0 #check varience of the column data
 
import pandas as pd
import numpy as np
df=pd.read_csv('C:/2-dataset/modified ethnic.csv.xls')


'''
create an imputer that creates NaN values
mean  and median is used for numeric data
mode is used for discrete data(position,sex,maritalDes)
'''

from sklearn.impute import SimpleImputer
mean_imputer = SimpleImputer(missing_values= np.nan ,strategy='mean')
                                        
#check the dataframe

df['Salararies'] = pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))


df['Salaries'].isna().sum()

