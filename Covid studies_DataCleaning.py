# -*- coding: utf-8 -*-
"""
Covid Studies 

Data Cleaning Part 

"""
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

df = pd.read_csv('C:/Users/GUORUI/Desktop/Graduate Bentley-desktop/2021 Spring/MA705/ClinialStudies.csv',low_memory=False)

#drop irrelevant columns
df.drop(df.iloc[:, 10:], inplace=True, axis=1)

##################recruiting status
# recuiting  ---Recruiting
# Active, not recruiting/ not yet recruiting/suspended  ---potential recruiting
# other recruiting 
#enrolling by invitation/completed/approved for marketing/terminated/withdrawn    ---Not recruiting



# #####################phase
#not-applicable/blank--without defined phase
#early --phase 0 
# phase0/1 --phase 1 and 0


#split location
s
#
