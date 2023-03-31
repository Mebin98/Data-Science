import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
# X = data.iloc[:,0:20] # independent columns, select all rows, and columns of 0~19
# y = data.iloc[:,-1] # target column, price_range, select all rows, and the last column 

# get correlation of pairs of features in the dataset
corrmat = data.corr() # corr() computes pairwise correlations of features in a Data Frame

top_corr_features = corrmat.index
plt.figure(figsize = (20,20))
# plot the heat map
corr_matrix = data[top_corr_features].corr()
sns.heatmap(corr_matrix, annot=True, cmap="RdYlGn")
plt.show()
