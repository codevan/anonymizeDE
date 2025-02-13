## Disclaimer and caution: This script/file was generated via generative AI 
####   Thursday February 13, 2025, without prejudice
##   Prompt: "..."

import pandas as pd
# Read the dataset into a pandas DataFrame
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0273EN-SkillsNetwork/labs/v1/m1/data/synthetic_dataset.csv')
print(df.head())
# Replace the entries under the 'Name' attribute with pseudonyms like "User_i"
df['Name'] = ['User_' + str(i) for i in range(1, len(df) + 1)]
# Function to redact email addresses
def redact_email(email):
    username, domain = email.split('@')
    redacted_username = username[0] + '*'*(len(username)-2) + username[-1]
    redacted_domain = domain[0] + '*'*(len(domain)-2) + domain[-1]
    return redacted_username + '@' + redacted_domain
# Redact 'Email' column in the dataframe
df['Email'] = df['Email'].apply(redact_email)
# Print the first 5 entries of the modified dataframe
print('Modified dataset')
print(df.head())