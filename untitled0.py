import pandas as pd
import numpy as np

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:03:01 2016

@author: danbiya
"""
messy = pd.DataFrame({'First':['John','Jane','Merry'],
                      'Last':['Smith','Doe','Johnshon'],
                      'Treatment A':[np.nan,16,3],
                      'Treatment B':[2,11,1]})

messy
#Transpose
messy.T
#show messy data

#tidying the data
tidy = pd.melt(messy,id_vars=['First','Last'])
tidy

messy1 = tidy.pivot(index='First', #return to original messy data
                    columns='variable',
                    values='value')

messy1.reset_index(inplace=True) #remove null variable
messy1

messy1.columns.name = ''
messy1

messy_r = pd.DataFrame({'Agnostic' : [27,34,60,81,76,137],
                      'Atheist' : [12,27,37,52,35,70],
                      'Buddhist' : [27,21,30,34,33,58],
                      'Catholic' : [410,627,732,670,638,1116] 
                      })

def transpose(df,columns): #transpose function
    df = df.T.copy()
    df.reset_index(inplace=True)
    df.columns = columns
    return df 
    
messy_r = transpose(messy, ['religion','$10k','$10-$20k','$20-30k','$30-40k'])

messy_r


df1 = pd.DataFrame({'key':['b','b','a','a','c','d','a'],
                 'data1' :range(7)
                 })
df2 = pd.DataFrame({'key':['a','b','d'],
                 'data2':range(3)})

df3 = pd.DataFrame({'key':['x','y','z','h','c','d','a'],
                 'data1' :range(7)
                 })
df4 = pd.DataFrame({'key':['z','x','h'],
                 'data2':range(3)})



pd.merge(df1,df2) #innerjoin

pd.merge(df3,df4, on='key', how='left')




tidy.sort_values
tidy.head() #peeking through dataset