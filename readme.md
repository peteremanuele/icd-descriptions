
# ICD Code Description Retrieval

This code provides functions to search for the description of a given ICD code in two different versions: ICD-9 and ICD-10. The code reads in two CSV files containing the codes and their respective descriptions, and uses pandas DataFrames to search for the desired code and return its description.

## Functions

### `getDescICD9(term, icd9_df)`

Given an ICD-9 code, this function returns its long description. If the code is not found, it returns "ICD-9 Not found".

### `getDescICD10(term, icd10_df)`

Given an ICD-10 code, this function returns its long description. If the code is not found, it returns "ICD-10 Not found".

### `validate_length(icd_code, version)`

Given an ICD code and its version (9 or 10), this function validates the length of the code and returns "Valid ICD-9 Length" or "Not Valid ICD Length" accordingly. 

## Usage

The code provides an example usage of the functions, where it defines two ICD codes and searches for their descriptions in both ICD-9 and ICD-10 versions. It also validates the length of the codes using the `validate_length` function.

To use the code with your own CSV files and ICD codes, replace the file paths and codes accordingly.