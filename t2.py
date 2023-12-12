import pandas as pd
import matplotlib.pyplot as plt
dataframe=pd.read_csv('data.csv')
plt.plot(dataframe)
plt.show()

#X=7
dataframe=pd.read_csv('data.csv',nrows=7)
plt.plot(dataframe)
plt.show()

#Y=14
dataframe=pd.read_csv('data.csv', usecols=['Durata','Puls'])
plt.plot(dataframe.tail(14))
plt.show()
