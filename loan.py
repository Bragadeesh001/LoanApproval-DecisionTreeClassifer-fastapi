from pydantic import BaseModel

#class which describes loanapproval measurement

class loanapproval(BaseModel):
    
    Gender: str
    Married: str
    Dependents: float
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float 
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: str
    Property_Area: str
    

