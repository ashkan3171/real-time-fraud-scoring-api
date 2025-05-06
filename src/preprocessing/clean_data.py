import pandas as pd

path = 'data/raw/raw_data.csv'

df = pd.read_csv(path)        # Load the data

new_df = df.drop(columns=['nameOrig', 'nameDest', 'isFlaggedFraud'])         #Remove irrelevant columns

print('HEAD:\n', new_df.head())
print('\nINFO:\n')
new_df.info()
print('\nMISSING VALUES:\n', new_df.isna().sum())
print('\nDUPLICATES:\n', new_df.duplicated().sum())
new_df = new_df.drop_duplicates()
print('\nTARGET DISTRIBUTION:\n', new_df['isFraud'].value_counts(normalize=True) * 100)
print('\nDESCRIBE:\n', new_df.describe())

output_path = 'data/processed/new_data.csv'
new_df.to_csv(output_path, index=False)
print(f'\nCleaned data saved to: {output_path}')  