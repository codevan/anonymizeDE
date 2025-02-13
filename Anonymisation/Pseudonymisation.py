## Disclaimer and caution: This script/file was generated via generative AI 
####   Thursday February 13, 2025, without prejudice
##   Prompt: "..."

import pandas as pd
# Read the dataset into a pandas DataFrame
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0273EN-SkillsNetwork/labs/v1/m1/data/synthetic_dataset.csv')
print(df.head())
# Replace the entries under the 'Name' attribute with pseudonyms like "User_i"
df['Name'] = ['User_' + str(i) for i in range(1, len(df) + 1)]
# Print the first 5 entries of the modified dataframe
print('Modified dataset')
print(df.head())