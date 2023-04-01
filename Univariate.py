import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.impute import SimpleImputer

# Load the dataset
data = pd.read_csv('housing.csv')

X = data.drop('median_house_value', axis=1)  # independent columns
y = data["median_house_value"]  # target column_median_house_value

X['longitude'] = X['longitude'].abs()  # transform to non-negative data

# one hot encoding to ocean_proximity
ocean_proximity_dummies = pd.get_dummies(X['ocean_proximity'], prefix='ocean_proximity')
X = pd.concat([X, ocean_proximity_dummies], axis=1)  # add to dataset
X = X.drop('ocean_proximity', axis=1)  # Remove from original dataset

# Handling missing values using mean imputation
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
X = pd.DataFrame(X_imputed, columns=X.columns)

# apply SelectBKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k = 10)
fit = bestfeatures.fit(X,y)
dfcolumns = pd.DataFrame(X.columns)
dfscores = pd.DataFrame(fit.scores_)

# concatenate two dataframes for better visualization
featureScores = pd.concat([dfcolumns,dfscores], axis = 1)
featureScores.columns = ['Specs', 'Score'] # name the dataframe columns

print(featureScores.nlargest(10,'Score')) # print 10 best features