# app.py
from flask import Flask, request, jsonify
from model import model_instance  # Import the model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data
    features = data['features']
    prediction = model_instance.predict([features])  # Make a prediction
    return jsonify({'prediction': int(prediction[0])})  # Return prediction

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
