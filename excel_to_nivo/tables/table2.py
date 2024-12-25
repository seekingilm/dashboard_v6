import pandas as pd

# Load the data
masterData = pd.read_excel('masterData.xlsx', index_col=0)

# Define the variables
main_variables_2 = [
    masterData['Q3) other_Role'],  
    masterData['Q3)  role_Manager'],
    masterData['Q3)  role_Owner'],
    masterData['Q3) role_Teacher'],
]

secondary_variables_2 = [
    masterData['Q10_Computer_Alert_words'], 
    masterData['Q10_Unknown_words'],
    masterData['Q10_Television_Radio_words'], 
    masterData['Q10_Parent_Guardian_words'],
    masterData['Q10_Other_words'],
    masterData['Q10_Supervisor_words'],
    masterData['Q10_Family_Friend_words'],
]

# Initialize an empty list to store the crosstabs
crosstabs_list = []

# Loop through the main variables and generate a crosstab for each with all secondary variables
for main_var in main_variables_2:
    # Create a dictionary to hold the counts for this main variable
    crosstab_dict = {}
    
    # Loop through each secondary variable and create the crosstab
    for sec_var in secondary_variables_2:
        crosstab_result = pd.crosstab(main_var, sec_var, dropna=False)
        # Store the result for this secondary variable in the dictionary
        crosstab_dict[sec_var.name] = crosstab_result
    
    # Combine all crosstab results into a single DataFrame for this main variable
    main_var_crosstab = pd.concat(crosstab_dict, axis=1)
    # Add the crosstab for this main variable to the list
    crosstabs_list.append(main_var_crosstab)

# Combine all the crosstabs for the main variables into one large contingency table
big_crosstab = pd.concat(crosstabs_list, keys=[var.name for var in main_variables_2], axis=0)

# Reset index if you want a cleaner index (optional)
big_crosstab.reset_index(drop=False, inplace=True)

# Display the final big contingency table
big_crosstab
