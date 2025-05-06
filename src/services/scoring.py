from src.services.explainer import generate_explanation

def score_transaction(transaction_df, model, threshold=0.95):

    prob = model.predict_proba(transaction_df)[:, 1][0]  # Get fraud probability
    is_fraud = int(prob >= threshold)
    transaction_dict = transaction_df.iloc[0].to_dict()
    explaination = generate_explanation(transaction_dict, fraud_probability=prob)

    return {
        'fraud_probability': float(prob),   # cast to native float
        'is_fraud': is_fraud,
        'explanation': explaination
    }