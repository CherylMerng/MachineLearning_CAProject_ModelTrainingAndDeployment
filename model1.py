import pickle
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv('iris-data-clean.csv').dropna()

# df.loc[df['class'] == 'Setosa', 'class'] = '0'
# df.loc[df['class'] == 'Virginica', 'class'] = '1'
# df.loc[df['class'] == 'Versicolor', 'class'] = '2'

# df_0 = df[df['class'] == 0 ]
# df_1 = df[df['class'] == 1 ]
# df_2 = df[df['class'] == 2 ]

logReg = LogisticRegression(solver = 'lbfgs')

x = df[['sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm']]
y = df['class']    # Classification : class = 0 or 1 or 2

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0) 

logReg.fit(x_train, y_train)

# deploy to the flask server
# flask server need to be started
pickle.dump(logReg, open('model1.pkl', 'wb'))  #serialize the object

# y_pred = logReg.predict(x_test)
# print(y_test)
# print(y_pred)