#library to be import
from fastapi import FastAPI
import uvicorn
import pickle
import numpy as np
import pandas as pd
from loan import loanapproval


#create the object and import the pickle file
app=FastAPI()
pickle_file=open('Loan_approval.pkl','rb')
classifier=pickle.load(pickle_file)

#index page
@app.get('/')
def index():
    return ("Hi, this is a program for loan approval model using fastapi")

@app.post('/predict')
def predict_loanapproval(data:loanapproval):
    data=data.dict()
    print(data)
    
    Gender=data['Gender']
    if Gender=='male':
        Gender=1
    else:
        Gender=0
    
    Married=data['Married']
    if Married=='yes':
        Married=1
    else:
        Married=0
      
    Education=data['Education']
    if Education=='yes':
         Education=0
    else:
         Education=1
         
    Self_Employed=data['Self_Employed']    
    if Self_Employed=='yes':
         Self_Employed=1
    else:
         Self_Employed=0
         
    Credit_History=data['Credit_History']
    if Credit_History=='yes':
         Credit_History=1
    else:
         Credit_History=0
         
    Property_Area=data['Property_Area']
    if Property_Area=='urban':
         Property_Area=2
    elif Property_Area=='rural':
        Property_Area=0
    else:
         Property_Area=1
         
    Dependents=data['Dependents']
    ApplicantIncome=data['ApplicantIncome']
    CoapplicantIncome=data['CoapplicantIncome']
    LoanAmount=data['LoanAmount']
    Loan_Amount_Term=data['Loan_Amount_Term']
         
     
    predict=classifier.predict([['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term', 'Credit_History', 'Property_Area']])
    
    if predict[0]>0.5:
        result='Loan is not approved'
    else:
       result='Loan is approved'
    return result

if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8080)