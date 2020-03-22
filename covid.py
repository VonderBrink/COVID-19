import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("C:/Users/user/Documents/GitHub/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv")
sortedTable = table.sort_values(by=['3/20/20'], ascending=False)
sortedTable = sortedTable[sortedTable['Country/Region'] == 'US']
#table = ff.create_table(df)

filteredSortedTable = sortedTable.head(3)
#print(filteredSortedTable[filteredSortedTable.columns[-30:]])
transpose = filteredSortedTable[filteredSortedTable.columns[-13:]].transpose()

print(filteredSortedTable)

print(transpose)

#y = filteredSortedTable['Country/Region']
#x = filteredSortedTable['3/20/20']

x1 = transpose[98]
x2 = transpose[99]
x3 = transpose[100]

#print(filteredSortedTable['Country/Region'])
#print(filteredSortedTable['3/20/20'])

#y = list(filteredSortedTable)
#y = filteredSortedTable[filteredSortedTable.columns[-3:]]
#x = list(filteredSortedTable.columns.values)


plt.figure(figsize=(15,6))
plt.plot(x1, label='New York')
plt.plot(x2, label='Washington')
plt.plot(x3, label='California')
plt.legend()

plt.show()