import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load the saved model pipeline
model = joblib.load('logistic_regression_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Parse the JSON data
    data = request.json
    df = pd.DataFrame(data)
    
    # Make predictions
    predictions = model.predict(df)
    
    # Return predictions as JSON
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
