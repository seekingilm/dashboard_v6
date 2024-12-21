from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to normalize the counts for each role
def normalize_counts(data):
    """
    Normalize the counts so that the sum of counts in each role is equal to 100%.
    """
    normalized_data = []

    # Iterate over each role's data
    for role_data in data:
        total_count = sum(role_data[col] for col in role_data if col != 'role')

        # Normalize each category
        normalized_role_data = {'role': role_data['role']}
        if total_count > 0:
            for col in role_data:
                if col != 'role':
                    normalized_role_data[col] = round((role_data[col] / total_count) * 100, 2)
        else:
            for col in role_data:
                if col != 'role':
                    normalized_role_data[col] = 0

        normalized_data.append(normalized_role_data)

    return normalized_data

@app.route("/bar1")
def process_clean_data_for_bar1():
    # Read the Excel file containing the raw data
    masterData = pd.read_excel('masterData.xlsx')

    # Print the column names to understand the structure
    print(masterData.columns)

    # Assuming the first column contains roles and subsequent columns contain counts for each alert word type
    roles = masterData['Role']  # Replace 'Role' with the actual column name for roles (e.g., 'Column1', 'Role', etc.)
    
    # Create a list of dictionaries with counts for each role
    data = []
    for i, role in enumerate(roles):
        role_data = {'role': role}
        for col in masterData.columns[1:]:  # Skip the first column which is the role column
            role_data[col] = masterData.iloc[i][col]
        data.append(role_data)

    # Normalize the counts
    normalized_data = normalize_counts(data)

    # Return the normalized data as JSON
    return jsonify(normalized_data)

if __name__ == '__main__':
    app.run(debug=True)
