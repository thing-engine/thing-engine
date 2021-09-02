# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('hiring.csv')

x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(x, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

#pass2

dts = pd.read_csv('solarpowergeneration.csv')
dts.head(10)

X = dts.iloc[:, :].values[:-1]
y = dts.iloc[:, -1].values[1:]
print(X.shape, y.shape)
y = np.reshape(y, (-1,1))
y.shape



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print("Train Shape: {} {} \nTest Shape: {} {}".format(X_train.shape, y_train.shape, X_test.shape, y_test.shape))


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X_train, y_train)

print(X_train)

# Saving model to disk
pickle.dump(regressor, open('model1.pkl','wb'))
