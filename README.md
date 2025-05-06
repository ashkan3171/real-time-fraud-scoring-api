# Real-Time LLM-Assisted Fraud Scoring API 🚨🧠

This project is a production-ready, real-time fraud detection system that combines machine learning (XGBoost) with an LLM-based explanation engine to score transactions and explain risky behavior in plain English.

---

## 🔍 Features

- ✅ Real-time fraud detection API using **FastAPI**
- ✅ Deployed as a **Docker container on AWS Lambda**
- ✅ **ML model (XGBoost)** for transaction risk scoring
- ✅ **LLM (e.g., GPT-4)** for generating human-readable fraud explanations
- ✅ Fully integrated with **AWS API Gateway**
- ✅ Tracks predictions, logs, and model versions using **CloudWatch** and **MLflow-ready structure**
- ✅ Containerized for scalable deployment

---

## 🏗️ Architecture Overview

1. **User/API** sends transaction data via HTTP `POST /predict`
2. **FastAPI** routes the request to the scoring engine
3. **XGBoost model** calculates fraud probability
4. **LLM layer** (OpenAI or Azure) explains why it’s fraudulent
5. API responds with:
   - fraud probability
   - is_fraud flag
   - natural language explanation

---

## 📦 Tech Stack

| Component       | Technology              |
|----------------|--------------------------|
| ML Model       | XGBoost                  |
| API Framework  | FastAPI + Mangum         |
| Model Serving  | AWS Lambda (container image) |
| Deployment     | Docker, ECR, API Gateway |
| Monitoring     | CloudWatch Logs          |
| LLM Integration| OpenAI GPT (via API)     |

---

## 🚀 Running Locally

1. Clone the repo:

```bash
git clone https://github.com/ashkan3171/real-time-fraud-scoring-api.git
cd real-time-fraud-scoring-api
```

2. Build and run the Docker container:

```bash
docker build -t fraud-api .
docker run -p 8000:8000 fraud-api
```

3. Test the API:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"amount": 200000, "diff_balanceOrig": 200000, "diff_balanceDest": 0, "late_phase": 1, "day": 800, "hour": 23, "type_CASH_IN": 0, "type_CASH_OUT": 0, "type_DEBIT": 0, "type_PAYMENT": 0, "type_TRANSFER": 1}'
```

---

## 🌐 Live Endpoint (via API Gateway)

```http
POST https://<your-api-id>.execute-api.eu-west-2.amazonaws.com/prod/predict
```

---

## 📁 Project Structure

```
.
├── src/
│   ├── api/              # FastAPI entrypoint (main.py)
│   └── services/         # score_transaction + LLM explanation
├── models/               # Trained XGBoost model (.joblib)
├── lambda_function.py    # Lambda entrypoint using Mangum
├── Dockerfile            # Container config for Lambda
├── .gitignore
└── requirements.txt
```

---

## 🤖 Example Response

```json
{
  "fraud_probability": 0.999,
  "is_fraud": 1,
  "explanation": "This transaction is highly suspicious due to the high amount, late timing, and use of a known fraud-prone type (TRANSFER)."
}
```

---

## 📌 TODOs

- [ ] Connect to real-time transaction stream (e.g., Kafka/SQS)
- [ ] Store scoring logs to S3 or DynamoDB
- [ ] Auto-retraining with MLflow & SageMaker pipelines

---

## 🧠 Author

Ashkan Sheikhansari  
[LinkedIn](https://linkedin.com/in/ashkan3171)  

---

## 📜 License

This project is licensed under the MIT License.
