from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Welcome to the Credit Card Fraud Detection API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    response = {'fraud': bool(prediction[0])}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)