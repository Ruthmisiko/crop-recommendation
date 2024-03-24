import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("./crop_recommendation.csv")

crop_summary=pd.pivot_table(data,index=['label'],aggfunc='mean')

# #removing outliers
df_boston = data.copy()  # Use a copy of the original data
df_boston.columns = df_boston.columns

'''Detecting Outliers'''

# #IQR
Q1 = np.percentile(df_boston['rainfall'], 25, interpolation='midpoint')
Q3 = np.percentile(df_boston['rainfall'], 75, interpolation='midpoint')
IQR = Q3 - Q1

print("Old Shape: ", df_boston.shape)

# #Upper bound
upper = np.where(df_boston['rainfall'] >= (Q3 + 1.5 * IQR))

# Lower bound
lower = np.where(df_boston['rainfall'] <= (Q1 - 1.5 * IQR))

'''Removing the Outliers '''
df_boston.drop(upper[0], inplace=True)
df_boston.drop(lower[0], inplace=True)



# pip install plotly
crop_summary_new=data.copy()

import random

# data.corr()

# ...
data.describe()
data.nunique()
data['label'].unique()
data['label'].value_counts()
crop_summary = pd.pivot_table(data, index=['label'], aggfunc='mean')
crop_summary
data.columns

#  computing correlation
numeric_corr = data.select_dtypes(include=[np.number]).corr()
print(numeric_corr)

# Analyzing data through plots
feature_cols = ['temperature', 'humidity', 'rainfall','label']
data = data[feature_cols]
X=data.drop('label',axis=1)
y=data['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.30, shuffle=True,random_state=0) 

import lightgbm as lgb
model = lgb.LGBMClassifier()
model.fit(X_train, y_train)

# Save model to pickle file 

filename = 'crop_model.pickle'
pickle.dump(model, open(filename, 'wb'))

# predictions on a single data point (for example, the first data point in X_test)
result = model.predict(X_test[0:1])

# Print or use the result as needed
print(result)

y_test[0:1]