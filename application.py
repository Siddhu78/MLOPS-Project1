import joblib
import numpy as np
from config.path_config import MODEL_OUTPUT_PATH
from flask import Flask, render_template, request

app=Flask(__name__)

loaded_model = joblib.load(MODEL_OUTPUT_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        try:

            lead_time =int(request.form["lead_time"])
            no_of_special_request = int(request.form["no_of_special_request"])
            avg_price_per_room = float(request.form["avg_price_per_room"])
            arrival_month = int(request.form["arrival_month"])
            arrival_date = int(request.form["arrival_date"])

            market_segment_type = int(request.form["market_segment_type"])
            no_of_week_nights = int(request.form["no_of_week_nights"])
            no_of_weekend_nights = int(request.form["no_of_weekend_nights"])

            type_of_meal_plan = int(request.form["type_of_meal_plan"])
            room_type_reserved = int(request.form["room_type_reserved"])

            features = np.array([[ lead_time,no_of_special_request,avg_price_per_room,arrival_month,arrival_date,market_segment_type,no_of_week_nights,no_of_weekend_nights,type_of_meal_plan,room_type_reserved]])

            prediction = loaded_model.predict(features)
            print("Prediction output:", prediction)


            return render_template('index.html', prediction=prediction[0])
        
        except Exception as e:
            print("❌ Error in POST request:", e)
            return render_template('index.html', prediction="Error: " + str(e))
    
    return render_template("index.html", prediction=None)
    

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)




