import pandas as pd
import numpy as np

h = pd.read_csv('Holdings.csv')
nav = pd.read_csv('NAV.csv')
meta = pd.read_csv('Meta_Data.csv')
#PART1

#extracting data from meta and holding
meta1 =(meta[(meta['Sub-Category'] == 'Large Cap Fund')]['Scheme Name']).to_list()
h1 = h[(h.iloc[0:,2:4].values == 'Domestic Equities')][['Unnamed: 1','202010']]

#filling nan values with mean()
h1['202010'] = h1['202010'].astype('float')
h1['202010'] = h1['202010'].fillna(h1['202010'].mean())


p1 = h1[(h1.iloc[:,0:1].values == meta1)][['Unnamed: 1','202010']]
s1 = p1['202010'].sum()
print("Holdings of all funds in Oct 2020 where the fund type is 'Large Cap' and asset is 'Domestic Equities' is",
      s1)


#PART2

#extracting data from meta and holding
meta2 =(meta[(meta['Sub-Category'] == 'Mid Cap Fund')]['Scheme Name']).to_list()
h2 = h.iloc[1:,np.r_[1,6:19]]

#changing the datatype
h2[['201911','201912','202001','202002','202003','202004','202005',
   '202006','202007','202008','202009','202010','202011']]= h2[['201911','201912',
                                                              '202001','202002','202003',
                                                              '202004','202005','202006',
                                                              '202007','202008','202009',
                                                              '202010','202011']].astype(float)

#creating a dataframe for specific data
p2 = h2[(h2.iloc[:,0:1].values == meta2)][['Unnamed: 1','201911','201912','202001','202002','202003','202004','202005',
   '202006','202007','202008','202009','202010','202011']]

s2 = p2.sum()
print("The average monthly returns of funds from Mar 2020 to Oct 2020 where fund type is 'Mid Cap'",s2.iloc[1:])
