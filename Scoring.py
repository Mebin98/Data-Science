import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.ensemble import ExtraTreesRegressor

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

model = ExtraTreesRegressor()
model.fit(X, y)

print(model.feature_importances_)  # use built-in class feature_importances of tree-based classifiers

# plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)

# Apply logarithm to feature importances
feat_importances = np.log(feat_importances)
feat_importances.nlargest(10).plot(kind='barh')  # horizontal bar
plt.show()