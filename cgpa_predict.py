#!C:\Users\celeron\AppData\Local\Programs\Python\Python39/python.exe
print ("Content-type: text/php\n\n");    

import cgi
from configparser import ConfigParser
import pandas as pd
import numpy as np
import pickle

form = cgi.FieldStorage()  

matricno = form.getvalue("matric_number")  #input comes from cgpa_form in php
sem1 = form.getvalue("sem1_cgpa")
sem2 = form.getvalue("sem2_cgpa")
sem3 = form.getvalue("sem3_cgpa")
sem4 = form.getvalue("sem4_cgpa")
sem5 = form.getvalue("sem5_cgpa")
sem6 = form.getvalue("sem6_cgpa")

def predict(sem, xnew):
    filename = "model" + str(sem) + '.sav'
    #loadmodel
    model = pickle.load(open(filename, 'rb'))
    results = model.predict(xnew)
    return results

#sample==========================================================
#predict new data - predict sem7 cgpa

numpy_array = np.array([[sem1, sem2, sem3, sem4, sem5, sem6]])
xnew = pd.DataFrame(numpy_array)
cgpa = predict(7, xnew)
cgpa = np.round_(cgpa,2)
result = cgpa[0]
print("Predicted Sem 7 CGPA: ", result)

#Connect to database
#store python output to database

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cgpa_prediction"
)

mycursor = mydb.cursor()

sql = "Insert INTO target (targetID, matric_number, predicted_cgpa) VALUES (%s, %s, %s )"
id = 0
matnum = matricno
val = (id,matnum,result)
mycursor.execute(sql, val)

print("Inserted value into database: ", val)
mydb.commit()
print("Your cgpa has been saved into database.")


