#The cgpa is predicted using MLPRegressor
#Data requirements: CGPA for each semester (cgpa_data.csv)

from sklearn.neural_network import  MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import pickle

def buildModel(sem, col):
    df = pd.read_csv('cgpa_data.csv') #read data from csv

    y = df.loc[:,col]
    x = df.drop(df.iloc[:, sem-1:6], axis = 1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = MLPRegressor(random_state=1, max_iter=500).fit(x_train, y_train)
    print(model.predict(x_test))
    print("Model Accuracy: " + str(model.score(x_test, y_test)))

    filename = 'Model' + str(sem) + '.sav' #save model
    pickle.dump(model, open(filename, 'wb'))

    sem = 7 #predict sem 7
    col = 'S7' 
    buildModel(sem,col)
