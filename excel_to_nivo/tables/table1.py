import pandas as pd

# Read the data from the Excel file
masterData = pd.read_excel('masterData.xlsx', index_col=0)

# Main variable and secondary variables
main_variables = [masterData['Q1.1.family_center']]  # If you have more main variables, add them to this list
secondary_variables = [
    masterData['Q12)Avoid_stove'], 
    masterData['Q12) central_AC'],
    masterData['Q12) Other_AC'],
    masterData['Q12) Close_W'],
    masterData['Q12) clean_indoor'],
    masterData['Q12)Cancel'],
    masterData['Q12) Portable_air'],
    masterData['Q12) Give_Masks'],
    masterData['Q12) Seal_WD (WD=Windows/Doors)']
]

# List to store the crosstab results
crosstabs_list = []

# Loop through the main variables and generate a crosstab for each with all secondary variables
for main_var in main_variables:
    # Create a dictionary to hold the counts for this main variable
    crosstab_dict = {}
    
    # Loop through each secondary variable and create the crosstab
    for sec_var in secondary_variables:
        crosstab_result = pd.crosstab(main_var, sec_var, dropna=False)
        # Store the result for this secondary variable in the dictionary
        crosstab_dict[sec_var.name] = crosstab_result
    
    # Combine all crosstab results into a single DataFrame for this main variable
    main_var_crosstab = pd.concat(crosstab_dict, axis=1)
    # Add the crosstab for this main variable to the list
    crosstabs_list.append(main_var_crosstab)

# Combine all the crosstabs for the main variables into one large contingency table
big_crosstab = pd.concat(crosstabs_list, keys=[var.name for var in main_variables], axis=0)

# Reset index if you want a cleaner index (optional)
big_crosstab.reset_index(drop=False, inplace=True)

# Display the final big contingency table
big_crosstab

