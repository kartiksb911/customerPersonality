from flask import Flask, render_template, request, jsonify
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        annual_income = float(request.form['annual_income'])
        spending_score = float(request.form['spending_score'])
        
        custom_data = CustomData(annual_income, spending_score)
        data = custom_data.get_data_as_dataframe()
        
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(data)
        
        return render_template('index.html', prediction=f"The predicted cluster is: {prediction[0]}")
    
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.get_json()
        annual_income = float(data['annual_income'])
        spending_score = float(data['spending_score'])
        
        custom_data = CustomData(annual_income, spending_score)
        df = custom_data.get_data_as_dataframe()
        
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(df)
        
        return jsonify({'prediction': str(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
