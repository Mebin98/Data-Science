import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

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

# Add target column back to the dataset
data_with_target = pd.concat([X, y], axis=1)

# get correlations of pairs of features in the dataset
corrmat = data_with_target.corr() #corr() computes pairwise correlations of features in a Data Frame
top_corr_features =corrmat.index
plt.figure(figsize = (10,10))

# plot the heat map
corr_matrix = data_with_target[top_corr_features].corr()
sns.heatmap(corr_matrix, annot=True, cmap="RdYlGn")
plt.show()