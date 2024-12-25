import pandas as pd

masterData = pd.read_excel('masterData.xlsx', index_col=0)

main_variable = masterData['Q1.1.family_center']

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

contingency_tables = []

for secondary_variable in secondary_variables:
    contingency_table = pd.crosstab(main_variable, secondary_variable, rownames=['Family Center'], colnames=[secondary_variable.name])
    contingency_tables.append(contingency_table)

combined_contingency_table = pd.concat(contingency_tables, axis=1)
print("Combined Contingency Table:\n", combined_contingency_table)

### table 2

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
    #masterData['Q10b_fire_over_cell_Words'],
]

contingency_tables_2 = []

for main_variable in main_variables_2:
    for secondary_variable in secondary_variables_2:
        contingency_table = pd.crosstab(main_variable, secondary_variable, rownames=[main_variable.name], colnames=[secondary_variable.name])
        contingency_tables_2.append(contingency_table)

combined_contingency_table_2 = pd.concat(contingency_tables_2, axis=1)
print("Combined Contingency Table 2:\n", combined_contingency_table_2)

### Table 3

main_variables_2 = [
    masterData['Q3) other_Role'],  # Replace with your actual variable names
    masterData['Q3)  role_Manager'],
    masterData['Q3)  role_Owner'],
    masterData['Q3) role_Teacher'],
]

secondary_variables_2 = [
    masterData['Q9_Other_words'],
    masterData['Q9a) event_Notification_Cellphone_Alert_WORDS'], 
    masterData['Q9_computer_Alert_news_WORDS'],
    masterData['Q9a) event_Notification_Cellphone_Alert_WORDS'],
    masterData['Q9_television_Radio_words'],
    masterData['Q9_Friends_Family_Words'],
    masterData['Q9_Unknown_Words'],
    masterData['Q9_Supervisor_Words'],
    masterData['Q9_Parent_Guardian_Words'],
]

contingency_tables_2 = []

# Create contingency tables for the second set of variables
for main_variable in main_variables_2:
    for secondary_variable in secondary_variables_2:
        contingency_table = pd.crosstab(main_variable, secondary_variable, rownames=[main_variable.name], colnames=[secondary_variable.name])
        contingency_tables_2.append(contingency_table)

combined_contingency_table_2 = pd.concat(contingency_tables_2, axis=1)
print("Combined Contingency Table 2:\n", combined_contingency_table_2)


