from fastapi import FastAPI
import uvicorn

import joblib

app = FastAPI()
model = joblib.load('pred_model')

from pydantic import BaseModel

class DataVar(BaseModel):

    gender: float

    SeniorCitizen: float

    Partner: float

    Dependents: float

    tenure: float

    PhoneService: float

    MultipleLines: float

    OnlineSecurity: float
    
    OnlineBackup: float

    DeviceProtection: float

    TechSupport  : float

    StreamingTV : float

    StreamingMovies: float


    PaperlessBilling: float


    MonthlyCharges: float

    TotalCharges: float

    InternetService_DSL : int
    
    InternetService_Fiberoptic: int
    
    InternetService_No: int
    
    c_Month: int
    
    c_Oneyear: int
    
    c_Twoyear: int
    
    PaymentMethod_Bank: int
    
    PaymentMethod_Credit: int
    
    PaymentMethod_Electronic: int
    
    PaymentMethod_Mailed: int


@app.get('/')
async def index():
  return {"text":"Our First route"}


@app.post('/prediction')

def get_prediction(data: DataVar):

    received = data.dict()

    gender = received['gender']

    SeniorCitizen= received['SeniorCitizen']

    Partner= received['Partner']

    Dependents= received['Dependents']

    tenure= received['tenure']

    PhoneService= received['PhoneService']

    MultipleLines= received['MultipleLines']

    OnlineSecurity= received['OnlineSecurity']

    OnlineBackup= received['OnlineBackup']

    DeviceProtection= received['DeviceProtection']

    TechSupport  = received['TechSupport']

    StreamingTV = received['StreamingTV']

    StreamingMovies= received['StreamingMovies']


    PaperlessBilling= received['PaperlessBilling']



    MonthlyCharges= received['MonthlyCharges']


    TotalCharges= received['TotalCharges']


    InternetService_DSL = received['InternetService_DSL']

    
    InternetService_Fiberoptic= received['InternetService_Fiberoptic']

    
    InternetService_No= received['InternetService_No']

    C_Month= received['c_Month']

    C_Oneyear= received['c_Oneyear']

    C_Twoyear= received['c_Twoyear']

    PaymentMethod_Bank= received['PaymentMethod_Bank']

    PaymentMethod_Credit= received['PaymentMethod_Credit']

    PaymentMethod_Electronic= received['PaymentMethod_Electronic']

    PaymentMethod_Mailed= received['PaymentMethod_Mailed']


    pred_name = model.predict([[gender, SeniorCitizen, Partner,

                                Dependents, tenure, PhoneService, MultipleLines, OnlineSecurity,
                                OnlineBackup, DeviceProtection, TechSupport, StreamingMovies, StreamingTV,
                                PaperlessBilling, MonthlyCharges, TotalCharges, InternetService_DSL,
                                InternetService_Fiberoptic, InternetService_No, C_Month,
                                C_Oneyear, C_Twoyear, PaymentMethod_Bank, 
                                PaymentMethod_Credit, PaymentMethod_Electronic, 
                                PaymentMethod_Mailed]]).tolist()[0]

    return {'prediction': pred_name}


if __name__ == '__main__':
  uvicorn.run(app,host="127.0.0.1",port=8000)