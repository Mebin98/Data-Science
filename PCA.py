import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

data = pd.read_csv('housing.csv') # load califnornia housing dataset

X = data.drop('median_house_value', axis=1)  # independent columns
y = data["median_house_value"]  # target column_median_house_value

# one hot encoding to ocean_proximity
ocean_proximity_dummies = pd.get_dummies(X['ocean_proximity'], prefix='ocean_proximity')
X = pd.concat([X, ocean_proximity_dummies], axis=1)  # add to dataset
X = X.drop('ocean_proximity', axis=1)  # Remove from original dataset

# Handling missing values using mean imputation
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
X = pd.DataFrame(X_imputed, columns=X.columns)

# Standardize the features
X = StandardScaler().fit_transform(X)

# PCA projection to 2D
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)
principalDf = pd.DataFrame(data = principalComponents,
                           columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, data[['median_house_value']]], axis = 1) # merge with target feature

fig = plt.figure(figsize = (8,8)) # draw a scatter plot
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
sc = ax.scatter(finalDf['principal component 1'], finalDf['principal component 2'], 
            c= data['median_house_value'], cmap= 'viridis', s=10, alpha=0.5)
ax.grid()

cbar = plt.colorbar(sc)
cbar.set_label('Median House Value', fontsize=15)
plt.show()