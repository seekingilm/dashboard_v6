from flask import Flask
import pandas as pd
from flask import jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def match_length(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    
    min_length = min(len1, len2)

    adjusted_arr1 = arr1[:min_length]
    adjusted_arr2 = arr2[:min_length]
    
    return adjusted_arr1, adjusted_arr2

def percentage_helper(list1, listy2):
    if(round(list1.corr(listy2), 2) < 0):
        return 0
    else:
        return round(list1.corr(listy2) * 100, 1) 

@app.route("/bar1")
def process_clean_data_for_bar1():
    masterData = pd.read_excel('masterData.xlsx', index_col=0)
    
    Owner = masterData['Q3)  role_Owner']
    Manager = masterData['Q3)  role_Manager']
    Teacher = masterData['Q3) role_Teacher']
    Other = masterData['Q3) other_Role']

    q9_phone = masterData['Q9a) event_Notification_Cellphone_Alert']
    q9_news = masterData['Q9_computer_Alert_news']
    q9_tv = masterData['Q9_television_Radio ']
    q9_family = masterData['Q9)friends_Family']
    q9_parent = masterData['Q9_parent_Guardian']
    q9_unknown = masterData['Q9) unknown_Q9']

    owner_np = Owner.to_numpy()[~np.isnan(Owner.to_numpy())]
    q9_phone_np = q9_phone.to_numpy()[~np.isnan(q9_phone.to_numpy())]
    owner_np, q9_phone_np = match_length(owner_np, q9_phone_np)

    roles_how_informed_data = [{
                    "role": "Owner", 
                    "phone": percentage_helper(Owner, q9_phone), 
                    "news": percentage_helper(Owner, q9_news),
                    "tv": percentage_helper(Owner, q9_tv),
                    "family": percentage_helper(Owner, q9_family),
                    "parent": percentage_helper(Owner, q9_parent),
                    "unknown": percentage_helper(Owner, q9_unknown),
                    },
                    {
                    "role": "Manager", 
                    "phone": percentage_helper(Manager, q9_phone), 
                    "news": percentage_helper(Manager, q9_news),
                    "tv": percentage_helper(Manager, q9_tv),
                    "family": percentage_helper(Manager, q9_family),
                    "parent": percentage_helper(Manager, q9_parent),
                    "unknown": percentage_helper(Manager, q9_unknown),
                    },
                    {
                    "role": "Teacher", 
                    "phone": percentage_helper(Teacher, q9_phone), 
                    "news": percentage_helper(Teacher, q9_news),
                    "tv": percentage_helper(Teacher, q9_tv),
                    "family": percentage_helper(Teacher, q9_family),
                    "parent": percentage_helper(Teacher, q9_parent),
                    "unknown": percentage_helper(Teacher, q9_unknown),
                    }, 
                    {
                        "role": "Other", 
                        "phone": percentage_helper(Other, q9_phone), 
                        "news": percentage_helper(Other, q9_news),
                        "tv": percentage_helper(Other, q9_tv),
                        "family": percentage_helper(Other, q9_family),
                        "parent": percentage_helper(Other, q9_parent),
                        "unknown": percentage_helper(Other, q9_unknown),
                    }
                   ]

    return jsonify(roles_how_informed_data)

@app.route("/bar2")
def process_clean_data_for_bar2():
    masterData = pd.read_excel('masterData.xlsx', index_col=0)

    Owner = masterData['Q3)  role_Owner']
    Manager = masterData['Q3)  role_Manager']
    Teacher = masterData['Q3) role_Teacher']
    Other = masterData['Q3) other_Role']

    Q10_Computer_Alert_words = masterData['Q10_Computer_Alert_words']
    Q10b_fire_over_cell_Words = masterData['Q10b_fire_over_cell_Words\n\n']
    Q10_Unknown_words = masterData['Q10_Unknown_words']
    Q10_Television_Radio_words = masterData['Q10_Television_Radio_words']
    Q10_Parent_Guardian_words = masterData['Q10_Parent_Guardian_words']
    Q10_Other_words = masterData['Q10_Other_words']
    Q10_Family_Friend_words = masterData['Q10_Family_Friend_words']
    Q10_Supervisor_words = masterData['Q10_Supervisor_words']

    roles_how_informed_data = [
            { "role": "Owner", 
             "cell_words": percentage_helper(Owner, Q10b_fire_over_cell_Words), 
             "tv": percentage_helper(Owner, Q10_Television_Radio_words), 
             "family": percentage_helper(Owner, Q10_Family_Friend_words),
             "parent": percentage_helper(Owner, Q10_Parent_Guardian_words),
             "unknown": percentage_helper(Owner, Q10_Unknown_words)
             },
            { "role": "Manager", 
             "cell_words": percentage_helper(Manager, Q10b_fire_over_cell_Words), 
             "tv": percentage_helper(Manager, Q10_Television_Radio_words), 
             "family": percentage_helper(Manager, Q10_Family_Friend_words),
             "parent": percentage_helper(Manager, Q10_Parent_Guardian_words),
             "unknown": percentage_helper(Manager, Q10_Unknown_words)
             },
            { "role": "Teacher", 
             "cell_words": percentage_helper(Teacher, Q10b_fire_over_cell_Words), 
             "tv": percentage_helper(Teacher, Q10_Television_Radio_words), 
             "family": percentage_helper(Teacher, Q10_Family_Friend_words),
             "parent": percentage_helper(Teacher, Q10_Parent_Guardian_words),
             "unknown": percentage_helper(Teacher, Q10_Unknown_words)
             },
            { "role": "Other", 
             "cell_words": percentage_helper(Other, Q10b_fire_over_cell_Words), 
             "tv": percentage_helper(Other, Q10_Television_Radio_words), 
             "family": percentage_helper(Other, Q10_Family_Friend_words),
             "parent": percentage_helper(Other, Q10_Parent_Guardian_words),
             "unknown": percentage_helper(Other, Q10_Unknown_words)
             }

    ]
   
    return jsonify(roles_how_informed_data)
 


if __name__ == '__main__':
        app.run(debug=True)
