import pandas as pd

def getDescICD9(term, icd9_df):
    # Remove period if present
    if '.' in term:
        term = term.replace('.', '')
    # Search for the term in the ICD-9 DataFrame
    try:
        desc = icd9_df.loc[icd9_df['CODE'] == term, 'LONG DESCRIPTION (VALID ICD-9 FY2023)'].iloc[0]
        return desc
    except IndexError:
        return "ICD-9 Not found"

def getDescICD10(term, icd10_df):
    # Remove period if present
    if '.' in term:
        term = term.replace('.', '')
    # Search for the term in the ICD-10 DataFrame
    try:
        desc = icd10_df.loc[icd10_df['CODE'] == term, 'LONG DESCRIPTION (VALID ICD-10 FY2023)'].iloc[0]
        return desc
    except IndexError:
        return "ICD-10 Not found"

# Define the function to detect the type of code entered
def validate_length(icd_code, version):
    icd_code = icd_code.replace(".", "") 
    if version == 9:
        if len(icd_code) in range(3, 6):
            return 'Valid ICD-9 Length'
        else:
            return 'Not Valid ICD-9 Length'
    else:
        if len(icd_code) in range(3, 8):
            return 'Valid ICD-10 Length'
        else:
            return 'Not Valid ICD-10 Length'


# Read in the CSV files as pandas DataFrames
icd9_df = pd.read_csv('icd9.csv')
icd10_df = pd.read_csv('icd10.csv')

# Define the code you want to search for
icd9_code = "789.00" # ICD-9 code for "Abdominal pain, unspecified site" 78900
icd10_code = "R10.9" # ICD-10 code for "Unspecified abdominal pain"

# Check valid length
icd9_length = validate_length(icd9_code, 9)
print("Validation of ICD-9", icd9_length )
icd10_length = validate_length(icd10_code, 10)
print("Validation of ICD-10", icd10_length )

# Search for the code in the respective sheet
icd_result = getDescICD9(icd9_code, icd9_df)
print("ICD-9 Description:", icd_result)

icd_result = getDescICD10(icd10_code, icd10_df)
print("ICD-10 Description:", icd_result)

