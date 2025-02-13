## Disclaimer and caution: This script/file was generated via generative AI 
####   Thursday February 13, 2025, without prejudice
# anonymizeDE dataframe IDCategoricalLabelEncode.py
#Prompt: Now using the same source URL, in a pandas dataframe, identify the categorical variables and perform label encoding on them, printing the first 5 entries to confirm it.

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the data from a source URL into a pandas DataFrame
url = 'your_source_url_here'  # Replace with your actual URL
df = pd.read_csv(url)

# Display the first few rows of the DataFrame to understand its structure
print("Initial DataFrame:")
print(df.head())

# Identify categorical variables
categorical_vars = df.select_dtypes(include=['object']).columns.tolist()

# Print identified categorical variables
print("\nIdentified Categorical Variables:")
print(categorical_vars)

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Apply label encoding to each categorical variable
for var in categorical_vars:
    # Check if the column is not already numeric
    if df[var].dtype == 'object':
        df[var] = label_encoder.fit_transform(df[var])
        print(f"\nLabel encoding applied to '{var}'.")

# Display the first 5 entries of the modified DataFrame
print("\nModified DataFrame (first 5 entries):")
print(df.head())

'''
#Example output

Initial DataFrame:
   Age  Gender  Total_Bilirubin  Direct_Bilirubin  Alkaline_Phosphotase  \
0   65  Female              0.7               0.1                   187   
1   62    Male             10.9               5.5                   699   
2   62    Male              7.3               4.1                   490   
3   58    Male              1.0               0.4                   182   
4   72    Male              3.9               2.0                   195   

   Alamine_Aminotransferase  Aspartate_Aminotransferase  Total_Proteins  \
0                        16                          18             6.8   
1                        64                         100             7.5   
2                        60                          68             7.0   
3                        14                          20             6.8   
4                        27                          59             7.3   

   Albumin  Albumin and Globulin Ratio  Selector  
0      3.3                        0.90         1  
1      3.2                        0.74         1  
2      3.3                        0.89         1  
3      3.4                        1.00         1  
4      2.4                        0.40         1  

Identified Categorical Variables:
['Gender']

Label encoding applied to 'Gender'.

Modified DataFrame (first 5 entries):
   Age  Gender  Total_Bilirubin  Direct_Bilirubin  Alkaline_Phosphotase  \
0   65       0              0.7               0.1                   187   
1   62       1             10.9               5.5                   699   
2   62       1              7.3               4.1                   490   
3   58       1              1.0               0.4                   182   
4   72       1              3.9               2.0                   195   

   Alamine_Aminotransferase  Aspartate_Aminotransferase  Total_Proteins  \
0                        16                          18             6.8   
1                        64                         100             7.5   
2                        60                          68             7.0   
3                        14                          20             6.8   
4                        27                          59             7.3   

   Albumin  Albumin and Globulin Ratio  Selector  
0      3.3                        0.90         1  
1      3.2                        0.74         1  
2      3.3                        0.89         1  
3      3.4                        1.00         1  
4      2.4                        0.40         1  

'''