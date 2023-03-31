# Features with higher scores are more important in predicting the target variable.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
X = data.iloc[:,0:20] # independent columns, select all rows, and columns of 0~19
y = data.iloc[:,-1] # target column, price_range, select all rows, and the last column 

from sklearn.ensemble import ExtraTreesClassifier 
# it is for extracting the top 10 features for the dataset

model = ExtraTreesClassifier()
model.fit(X,y) # train the model

print(model.feature_importances_)
# use built-in class feature_importances of tree-based classifiers

# plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_,index=X.columns)
feat_importances.nlargest(10).plot(kind='barh') #horizontal bar
plt.show()