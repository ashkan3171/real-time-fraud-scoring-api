from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel 
from src.services.scoring import score_transaction
import joblib
from mangum import Mangum

# Initialize API
app = FastAPI(title='Real-Time Fraud Scoring API')

# Load trained model
model = joblib.load('src/models/xgb_model.joblib')  # adjust path if needed

handler = Mangum(app)

class Transaction(BaseModel):
    amount: float
    diff_balanceOrig: float
    diff_balanceDest: float
    late_phase: int
    day: int
    hour: int
    type_CASH_IN: int
    type_CASH_OUT: int
    type_DEBIT: int
    type_PAYMENT: int
    type_TRANSFER: int

@app.post('/predict')
def predict_fraud(tx: Transaction):
    tx_dict = tx.dict()
    tx_df = pd.DataFrame([tx_dict])
    result = score_transaction(tx_df, model, threshold=0.95)
    return result   