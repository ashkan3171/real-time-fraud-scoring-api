def generate_explanation(transaction: dict, fraud_probability: float) -> str:
    reasons = []

    if transaction['amount'] > 100000:
        reasons.append("the transaction amount is unusually high")

    if transaction['type_TRANSFER'] == 1 or transaction['type_CASH_OUT'] == 1:
        reasons.append("it uses a transaction type commonly linked to fraud (TRANSFER or CASH_OUT)")

    if transaction['late_phase'] == 1:
        reasons.append("it occurred during a suspicious time window (late phase)")

    if transaction['diff_balanceDest'] == 0:
        reasons.append("the destination account did not receive the expected funds")

    if not reasons:
        reasons.append("it shows minor similarities with known fraud cases")

    # Severity message based on fraud probability
    if fraud_probability > 0.99:
        severity = "This transaction is highly suspicious"
    elif fraud_probability > 0.95:
        severity = "This transaction is likely fraudulent"
    elif fraud_probability > 0.80:
        severity = "This transaction may be suspicious"
    else:
        severity = "This transaction appears to be safe"

    return f"{severity} because " + ", ".join(reasons) + "."
