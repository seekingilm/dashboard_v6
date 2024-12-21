from flask import Flask
import pandas as pd
from flask import jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def percentage_helper(list1, listy2):
    if round(list1.corr(listy2), 2) < 0:
        return 0
    else:
        return round(round(list1.corr(listy2), 2) * len(list1), 2)

def percentage_maker(full_db, role, segment):
    count = 0

    for i in range(len(full_db) - 1):
        row = full_db[i: i + 1]

        value_role = float(row[role].values)
        value_segment = float(row[segment].values)

        if value_role == value_segment and value_segment == 1:
            count = count + 1

    total_role = len(full_db)
    return_value = count / total_role

    return round(round(count / total_role, 2) * 100)

def normalize_data(data):
   for role_data in data:
        total_percentage = sum(role_data[category] for category in role_data if category != "role")
        if total_percentage > 0:
            for category in role_data:
                if category != "role":
                    role_data[category] = round((role_data[category] / total_percentage) * 100, 2)
    return data

@app.route("/bar1")
def process_clean_data_for_bar1():
    masterData = pd.read_excel('masterData.xlsx', index_col=0)
    
    Owner = 'Q3)  role_Owner'
    Manager = 'Q3)  role_Manager'
    Teacher = 'Q3) role_Teacher'
    Other = 'Q3) other_Role'

    q9_phone = 'Q9a) event_Notification_Cellphone_Alert'
    q9_news = 'Q9_computer_Alert_news'
    q9_tv = 'Q9_television_Radio '
    q9_family = 'Q9)friends_Family'
    q9_parent = 'Q9_parent_Guardian'
    q9_unknown = 'Q9) unknown_Q9'

    # Collecting data for each role
    roles_how_informed_data = [{
                    "role": "Owner", 
                    "phone": percentage_maker(masterData, Owner, q9_phone), 
                    "news": percentage_maker(masterData, Owner, q9_news),
                    "tv": percentage_maker(masterData, Owner, q9_tv),
                    "family": percentage_maker(masterData, Owner, q9_family),
                    "parent": percentage_maker(masterData, Owner, q9_parent),
                    "unknown": percentage_maker(masterData, Owner, q9_unknown),
                    },
                    {
                    "role": "Manager", 
                    "phone": percentage_maker(masterData, Manager, q9_phone), 
                    "news": percentage_maker(masterData, Manager, q9_news),
                    "tv": percentage_maker(masterData, Manager, q9_tv),
                    "family": percentage_maker(masterData, Manager, q9_family),
                    "parent": percentage_maker(masterData, Manager, q9_parent),
                    "unknown": percentage_maker(masterData, Manager, q9_unknown),
                    },
                    {
                    "role": "Teacher", 
                    "phone": percentage_maker(masterData, Teacher, q9_phone), 
                    "news": percentage_maker(masterData, Teacher, q9_news),
                    "tv": percentage_maker(masterData, Teacher, q9_tv),
                    "family": percentage_maker(masterData, Teacher, q9_family),
                    "parent": percentage_maker(masterData, Teacher, q9_parent),
                    "unknown": percentage_maker(masterData, Teacher, q9_unknown),
                    }, 
                    {
                    "role": "Other", 
                    "phone": percentage_maker(masterData, Other, q9_phone), 
                    "news": percentage_maker(masterData, Other, q9_news),
                    "tv": percentage_maker(masterData, Other, q9_tv),
                    "family": percentage_maker(masterData, Other, q9_family),
                    "parent": percentage_maker(masterData, Other, q9_parent),
                    "unknown": percentage_maker(masterData, Other, q9_unknown),
                    }, 
                   ]

    # Normalize the data
    normalized_data = normalize_data(roles_how_informed_data)

    return jsonify(normalized_data)


if __name__ == '__main__':
    app.run(debug=True)
