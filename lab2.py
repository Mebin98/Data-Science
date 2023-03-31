import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest # for use with some satistical test... 
from sklearn.feature_selection import chi2 

data = pd.read_csv('train.csv')
X = data.iloc[:,0:20] # independent columns, select all rows, and columns of 0~19
y = data.iloc[:,-1] # target column, price_range, select all rows, and the last column 

# apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k = 10) # with using chi-squared test, excutes feature selection, select 10 important features
fit = bestfeatures.fit(X,y) # train model
dfcolumns = pd.DataFrame(X.columns) # extract column name of 'X' object, and create dfcolumns
dfscores = pd.DataFrame(fit.scores_) # fit.scores_ is numpy array that showing score of each features

# concatenate two dataframes for bettwe visualization

featureScores = pd.concat([dfcolumns,dfscores], axis = 1)
featureScores.columns = ['Specs','Score'] # name the dataframe columns
print(featureScores.nlargest(10,'Score')) # print 10 best features

