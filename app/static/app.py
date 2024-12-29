from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

# Dummy time-series prediction function
def predict_energy_usage(data):
    return {
        "predicted_bill": round(np.random.uniform(50, 150), 2),
        "suggestions": [
            "Use energy-efficient appliances",
            "Turn off lights when not in use",
            "Consider solar panels for long-term savings"
        ]
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    predictions = predict_energy_usage(data)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
