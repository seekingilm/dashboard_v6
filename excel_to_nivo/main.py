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

def percentage_helper(corr):
    if(corr < 0):
        return 0
    else:
        corr * 100

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
    
    #table1 = pd.crosstab(index=owner_np, columns=q9_phone_np) # this is a contingency table
    #overall_proportions = table1 / table1.sum().sum()

    print(Owner.corr(q9_phone))

    roles_how_informed_data = [{
                    "role": "Owner", 
                    "phone": round(Owner.corr(q9_phone), 2), 
                    "news": round(Owner.corr(q9_news), 2),
                    "tv": round(Owner.corr(q9_tv),2),
                    "family": round(Owner.corr(q9_family),2),
                    "parent": round(Owner.corr(q9_parent), 2),
                    "unkown": round(Owner.corr(q9_unknown),2),
                    },
                    {
                    "role": "Manager", 
                    "phone": round(Manager.corr(q9_phone), 2), 
                    "news": round(Manager.corr(q9_news), 2),
                    "tv": round(Manager.corr(q9_tv),2),
                    "family": round(Manager.corr(q9_family),2),
                    "parent": round(Manager.corr(q9_parent), 2),
                    "unkown": round(Manager.corr(q9_unknown),2),
                    },
                    {
                    "role": "Teacher", 
                    "phone": round(Teacher.corr(q9_phone), 2), 
                    "news": round(Teacher.corr(q9_news), 2),
                    "tv": round(Teacher.corr(q9_tv),2),
                    "family": round(Teacher.corr(q9_family),2),
                    "parent": round(Teacher.corr(q9_parent), 2),
                    "unkown": round(Teacher.corr(q9_unknown),2),
                    },
                    {
                    "role": "Other", 
                    "phone": round(Other.corr(q9_phone), 2), 
                    "news": round(Other.corr(q9_news), 2),
                    "tv": round(Other.corr(q9_tv),2),
                    "family": round(Other.corr(q9_family),2),
                    "parent": round(Other.corr(q9_parent), 2),
                    "unkown": round(Other.corr(q9_unknown),2),
                    }
                   ]

    return jsonify(roles_how_informed_data)


if __name__ == '__main__':
        app.run(debug=True)
