import numpy as np
from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

# Load the trained model pipeline
base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, 'model', 'breast_cancer_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form in exact order of training
        features = [
            float(request.form['radius_mean']),
            float(request.form['texture_mean']),
            float(request.form['perimeter_mean']),
            float(request.form['area_mean']),
            float(request.form['smoothness_mean'])
        ]

        # Convert to numpy array
        final_features = [np.array(features)]
        
        # Predict using the pipeline (Scaler + SVM)
        # 0 = Malignant, 1 = Benign in sklearn dataset
        prediction = model.predict(final_features)
        
        if prediction[0] == 0:
            text = "Result: MALIGNANT (Consult a Doctor)"
            css_class = "malignant"
        else:
            text = "Result: BENIGN (Safe)"
            css_class = "benign"
            
        return render_template('index.html', prediction_text=text, result_class=css_class)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", result_class="malignant")

if __name__ == "__main__":
    app.run(debug=True)