## Disclaimer and caution: This script/file was generated via generative AI 
####   Thursday February 13, 2025, without prejudice
##   Prompt: "..."

import pandas as pd
# Read the dataset into a pandas DataFrame
df = pd.read_csv('https://example.com/replace-with-own-data/synthetic_dataset.csv')
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
# Function to generalize age
def generalize_age(age):
    age_range = str(age)[0] + '0s'
    return age_range
# Generalize 'Age' column in the dataframe
df['Age'] = df['Age'].apply(generalize_age)
# Print the first 5 entries of the modified dataframe
print('Modified dataset')
print(df.head())