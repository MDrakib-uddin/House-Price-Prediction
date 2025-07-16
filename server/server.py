# app.py

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.form
    location = data['location']
    total_sqft = float(data['total_sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
