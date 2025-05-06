import pandas as pd
from sklearn.preprocessing import OneHotEncoder

path = 'data/processed/eda_data.csv'

df = pd.read_csv(path)
new_df = df.drop(columns=['step', 'oldbalanceOrg', 'newbalanceOrig', 'newbalanceDest', 'oldbalanceDest'])

encoder = OneHotEncoder(sparse_output=False)
one_hot_encode  = encoder.fit_transform(new_df[['type']])
encoded_cols = encoder.get_feature_names_out(['type'])
encoded_df = pd.DataFrame(one_hot_encode, columns=encoded_cols)
new_df = pd.concat([new_df.drop(columns='type'), encoded_df], axis=1)

new_df['late_phase'] = new_df['late_phase'].astype(int)

print(new_df.head())

output_path = 'data/processed/featured_data.csv'
new_df.to_csv(output_path, index=False)