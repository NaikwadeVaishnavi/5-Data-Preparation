# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:58:53 2023

@author: DELL5300 2IN -1
"""

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('C:/2-dataset/Boston.csv')

df.shape

df.columns

df.dtypes

df_dup = df.duplicated()
sum(df_dup)
#no duplicate value present

sns.boxplot(df.crim)
#outliers are present

#outlier treatement 
IQR = df.crim.quantile(0.75) - df.crim.quantile(0.25)
IQR

lower_limit = df.crim.quantile(0.25) - 1.5 * IQR
#-5.31051125 make it 0
upper_limit = df.crim.quantile(0.25) + 1.5 * IQR
#5.47460125

#trimming
outliers_df = np.where(df.crim > upper_limit, True , np.where(df.crim < lower_limit ,True, False))
sum(outliers_df)
#102 pts are outlier
# u can check outliers_df column in variable explorer
df_trimmed = df.loc[~outliers_df]
df.shape
# (506, 15)
df_trimmed.shape
#(404, 15)


#replacement technique

df=pd.read_csv("C:/2-dataset/Boston.csv")
df.describe

#356 record has outlier


df_replaced = pd.DataFrame(np.where(df.crim > upper_limit, upper_limit, np.where(df.crim < lower_limit ,lower_limit , df.crim)))
sns.boxplot(df_replaced[0])
