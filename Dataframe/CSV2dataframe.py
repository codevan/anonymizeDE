## Disclaimer and caution: This script/file was generated via generative AI 
####   Thursday February 13, 2025, without prejudice
# anonymizeDE dataframe CSV2dataframe.py
#   Prompt: "Write a Python code that reads a CSV file from a URL into a Pandas dataframe, and prints the first 5 entries to confirm it."

import pandas as pd
def read_csv_from_url(url):
    """
    Reads a CSV file from the specified URL into a Pandas DataFrame.
    Parameters:
        url (str): The URL of the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    try:
        # Read the CSV file from the URL
        df = pd.read_csv(url)
        return df

    except Exception as e:
        # Handle exceptions that may occur during the reading process
        print(f"An error occurred while reading the CSV file: {e}")
        return None


def main():
    # URL of the CSV file
    csv_url = "https://example.com/data.csv"  # Replace with the actual URL

    # Read the CSV file into a DataFrame
    dataframe = read_csv_from_url(csv_url)

    if dataframe is not None:
        # Print the first 5 entries of the DataFrame
        print("First 5 entries of the DataFrame:")
        print(dataframe.head())
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    main()


'''
Example output from the Indian Liver Patient Dataset:

First 5 entries of the DataFrame:
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


'''