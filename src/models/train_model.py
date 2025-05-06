import pandas  as pd
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load features
X_train = pd.read_csv('data/splits/X_train.csv')
X_test = pd.read_csv('data/splits/X_test.csv')

# Load labels
y_train = pd.read_csv('data/splits/y_train.csv').squeeze()
y_test = pd.read_csv('data/splits/y_test.csv').squeeze()

# Initialize model
model = XGBClassifier(
     n_estimators=100,
     max_depth = 5,
     learning_rate = 0.1, 
     use_label_encoder=False,
     eval_metric='logloss',
     scale_pos_weight=(len(y_train) - sum(y_train)) / sum(y_train)  # handle imbalance
)

#Train
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'src/models/xgb_model.joblib')

#Evaluate
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # Get fraud probability


thresholds = [0.5, 0.7, 0.9, 0.95, 0.99]
for t in thresholds:
    print(f'\n Threshold: {t}')
    y_pred_thresh = (y_proba >= t).astype(int)
    print(classification_report(y_test, y_pred_thresh, digits=4))
    print('\n Confusion Matrix:')
    print(confusion_matrix(y_test, y_pred_thresh))