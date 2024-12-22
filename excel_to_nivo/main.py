from flask import Flask
import pandas as pd
from flask import jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def percentage_maker(full_db, role, segement):
    count = 0
    bar1_set = ['Q9a) event_Notification_Cellphone_Alert','Q9_computer_Alert_news', 
                'Q9_television_Radio ','Q9)friends_Family','Q9_parent_Guardian','Q9) unknown_Q9']

    if segement in bar1_set:
        for i in range(len(full_db)-1):
            row = full_db[i: i+1]

            value_role = float(row[role].values) 
            value_segement = float(row[segement].values)

            if(value_role == value_segement and value_segement == 1):
                count = count + 1
    else:
        for i in range(len(full_db)-1):
            row = full_db[i: i+1]

            if('[nan]' != str(row[segement].to_numpy()) and float(row[role].to_numpy()) == 1.0):
                print(f"the segement is {str(row[segement].to_numpy())} and the role is {float(row[role].to_numpy())}")
                count = count + 1

    print(count)
    return count 

def object_normalizer(item):
    total = item['parent'] + item['unknown'] + item['tv'] + item['phone'] + item['news'] + item['family']; 
    
    item['phone'] = round(round(item['phone']/total,2) * 100)
    item['news'] = round(round(item['news']/total, 2) * 100)
    item['tv'] = round(round(item['tv']/total, 2) * 100)
    item['family'] = round(round(item['family']/total, 2) * 100)
    item['parent'] = round(round(item['parent']/total, 2) * 100)
    item['unknown'] = round(round(item['unknown']/total, 2) * 100)

    return item

def object_normalizer_bar2(item):
    total = item['radio'] + item['parent'] + item['others_words'] + item['supervisor'] + item['family'] 
    print(total)
    
    item['radio'] = round(round(item['radio']/total,3) * 100)
    item['parent'] = round(round(item['parent']/total, 2) * 100)
    item['others_words'] = round(round(item['others_words']/total, 2) * 100)
    item['supervisor'] = round(round(item['supervisor']/total, 2) * 100)
    item['family'] = round(round(item['family']/total, 2) * 100)

    return item

@app.route("/bar1")
def process_clean_data_for_bar1():
    masterData = pd.read_excel('masterData.xlsx', index_col=0)
    print(percentage_maker(masterData, 'Q3)  role_Owner', 'Q9a) event_Notification_Cellphone_Alert'))
    print(percentage_maker(masterData, 'Q3)  role_Owner', 'Q9_computer_Alert_news'))
    
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

    #pd.crosstab(Q9_computer_Alert_words, Other)
    
    roles_how_informed_data = [object_normalizer({
                    "role": "Owner", 
                    "phone": percentage_maker(masterData, Owner, q9_phone), 
                    "news": percentage_maker(masterData, Owner, q9_news),
                    "tv": percentage_maker(masterData, Owner, q9_tv),
                    "family": percentage_maker(masterData, Owner, q9_family),
                    "parent": percentage_maker(masterData, Owner, q9_parent),
                    "unknown": percentage_maker(masterData, Owner, q9_unknown),
                    }),
                    object_normalizer({
                    "role": "Manager", 
                    "phone": percentage_maker(masterData, Manager, q9_phone), 
                    "news": percentage_maker(masterData, Manager, q9_news),
                    "tv": percentage_maker(masterData, Manager, q9_tv),
                    "family": percentage_maker(masterData, Manager, q9_family),
                    "parent": percentage_maker(masterData, Manager, q9_parent),
                    "unknown": percentage_maker(masterData, Manager, q9_unknown),
                    }),
                    object_normalizer({
                    "role": "Teacher", 
                    "phone": percentage_maker(masterData, Teacher, q9_phone), 
                    "news": percentage_maker(masterData, Teacher, q9_news),
                    "tv": percentage_maker(masterData, Teacher, q9_tv),
                    "family": percentage_maker(masterData, Teacher, q9_family),
                    "parent": percentage_maker(masterData, Teacher, q9_parent),
                    "unknown": percentage_maker(masterData, Teacher, q9_unknown),
                    }), 
                    object_normalizer({
                    "role": "Other", 
                    "phone": percentage_maker(masterData, Other, q9_phone), 
                    "news": percentage_maker(masterData, Other, q9_news),
                    "tv": percentage_maker(masterData, Other, q9_tv),
                    "family": percentage_maker(masterData, Other, q9_family),
                    "parent": percentage_maker(masterData, Other, q9_parent),
                    "unknown": percentage_maker(masterData, Other, q9_unknown),
                    }), 
                   ]

    return jsonify(roles_how_informed_data)

@app.route("/bar2")
def process_clean_data_for_bar2():
    masterData = pd.read_excel('masterData.xlsx', index_col=0)

    Owner = 'Q3)  role_Owner'
    Manager = 'Q3)  role_Manager'
    Teacher = 'Q3) role_Teacher'
    Other = 'Q3) other_Role'

    Q10_Television_Radio_words = 'Q10_Television_Radio_words'
    Q10_Parent_Guardian_words = 'Q10_Parent_Guardian_words'
    Q10_Other_words = 'Q10_Other_words'
    Q10_Family_Friend_words = 'Q10_Family_Friend_words'
    Q10_Supervisor_words = 'Q10_Supervisor_words'
    
    roles_how_informed_data = [object_normalizer_bar2({
                    "role": "Owner", 
                    "radio": percentage_maker(masterData, Owner, Q10_Television_Radio_words ), 
                    "parent": percentage_maker(masterData, Owner,Q10_Parent_Guardian_words),
                    "others_words": percentage_maker(masterData, Owner, Q10_Other_words ),
                    "supervisor": percentage_maker(masterData, Owner, Q10_Supervisor_words),
                    "family": percentage_maker(masterData, Owner, Q10_Family_Friend_words ),
                    }),
                    object_normalizer_bar2({
                    "role": "Manager", 
                    "radio": percentage_maker(masterData, Manager, Q10_Television_Radio_words ), 
                    "parent": percentage_maker(masterData, Manager,Q10_Parent_Guardian_words),
                    "others_words": percentage_maker(masterData, Manager, Q10_Other_words ),
                    "supervisor": percentage_maker(masterData, Manager, Q10_Supervisor_words),
                    "family": percentage_maker(masterData, Manager, Q10_Family_Friend_words ),
                    }),
                    object_normalizer_bar2({
                    "role": "Teacher", 
                    "radio": percentage_maker(masterData, Teacher, Q10_Television_Radio_words ), 
                    "parent": percentage_maker(masterData, Teacher,Q10_Parent_Guardian_words),
                    "others_words": percentage_maker(masterData, Teacher, Q10_Other_words ),
                    "supervisor": percentage_maker(masterData, Teacher, Q10_Supervisor_words),
                    "family": percentage_maker(masterData, Teacher, Q10_Family_Friend_words ),
                    }), 
                    object_normalizer_bar2({
                    "role": "Other", 
                    "radio": percentage_maker(masterData, Other, Q10_Television_Radio_words ), 
                    "parent": percentage_maker(masterData, Other,Q10_Parent_Guardian_words),
                    "others_words": percentage_maker(masterData, Other, Q10_Other_words ),
                    "supervisor": percentage_maker(masterData, Other, Q10_Supervisor_words),
                    "family": percentage_maker(masterData, Other, Q10_Family_Friend_words ),
                    }), 
                   ]

    return jsonify(roles_how_informed_data)
