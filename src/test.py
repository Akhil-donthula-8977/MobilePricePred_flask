from flask import Blueprint, request, jsonify
import pickle
import os
import numpy as np
import pandas as pd

predict = Blueprint("predict", __name__, url_prefix="/predict")

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@predict.post("/test")
def Home():
    data_columns=['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
       'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
       'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
       'touch_screen', 'wifi']
    
    input_values=[]
    for feature in data_columns:
        input_values.append(float(request.json[feature]))
    
    ans=model.predict(pd.DataFrame([input_values], columns=data_columns))
    ans_list = ans.tolist()
    return jsonify({"prediction": ans_list})
