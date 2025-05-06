import os   
import pandas as pd
from sklearn.model_selection import train_test_split

path = 'data/processed/featured_data.csv'
df = pd.read_csv(path)


X = df.drop(columns='isFraud')
y = df['isFraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

os.makedirs('data/splits', exist_ok=True)
X_train.to_csv('data/splits/X_train.csv', index=False)
X_test.to_csv('data/splits/X_test.csv', index=False)
y_train.to_csv('data/splits/y_train.csv', index=False)
y_test.to_csv('data/splits/y_test.csv', index=False)