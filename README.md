# Customer Segmentation with KMeans Clustering
## Introduction:-
This project performs customer segmentation based on annual income and spending score using the KMeans clustering algorithm. It involves multiple stages: data ingestion, data transformation, model training, and predictions. The model is deployed using a Flask web application that allows users to make predictions through both a web interface and API.

## Steps Involved
* **Data Ingestion**:The DataIngestion module reads the raw data from the CSV file and performs basic preprocessing by dropping unnecessary columns.
* **DataTransformation**:The DataTransformation module scales the features (Annual Income and Spending Score) using StandardScaler.
* **ModelTrainer**:The ModelTrainer module trains the KMeans clustering model, performing clustering with 5 clusters. It also calculates the silhouette score to evaluate the model’s performance.
* **Web Application (Flask)**:A simple Flask web application is used to interact with the trained model. Users can input their annual income and spending score, and the app will predict the customer cluster based on the trained model.
* **Routes**:
* /: Home route that displays the index page (index.html).
* /predict: POST route where users can input their data to get cluster predictions.
* /predict_api: API route that accepts a JSON object with the data and returns the prediction.
* **Deployed**: Deployed the app to `Render` for easy access and hosting.
*  **Model Prediction**: The model is saved in the `artifacts/model.pkl` file, and when a user submits data through the web app, the Flask app loads the model and uses it to predict the customer cluster.
* **Saving Model and Scaler**:Both the trained KMeans model and the `StandardScaler` used for preprocessing are saved to disk (model.pkl and scaler.pkl), ensuring they can be reused in future predictions without retraining.
## Technology Used
* machine learning model-->`KMeans`
* web framework-->`Flask` and `html`
* Version Control-->`Git` and `Github`
* code editors-->`jupyter lab `and `Vscode`
* python library-->`numpy`,`Pandas`,`Matplotlib`,`seaborn`,`sklearn`
## How to run:
#### Clone the Repository

To clone this repository, run the following command:

```
git clone https://github.com/kartiksb911/customerPersonality.git
```
#### Create a new environment for the project and activate it.
```
 conda create -p venv python=3.10 -y
 conda activate venv/
```
#### Install all necessary requirements
``` 
pip install -r requirements.txt
```
#### Train the Model
Run the following code to start the data ingestion process and train the model:

``` 
python main.py
```
* After running this code, the model will be trained.
#### Test the Web Application:
Once the model is trained, you can start the Flask web app by running:
``` 
python app.py
```
Visit http://127.0.0.1:5000 in your browser to interact with the web app.

## Link of deployed Web App:
```
https://client-cluster.onrender.com
```
## Make Predictions:
* *Web Interface*: Open the web app in your browser and input the data (Annual Income and Spending Score) to get the predicted cluster.
* *API*: You can also make a POST request to /predict_api with a JSON payload like:
```
{
  "annual_income": 60,
  "spending_score": 40
}
```
## Data Flow:
* Raw data is ingested and preprocessed by the DataIngestion module.
* The data is then scaled using StandardScaler in the DataTransformation module.
* The scaled data is passed to the ModelTrainer, where the KMeans model is trained on it and saved.
## Web Interaction:
* Users can input data through the Flask application.
* The CustomData class formats the input data, and the PredictPipeline class predicts the cluster.
* The result is displayed in the web interface or returned as a JSON response.
### Web App
![Image Alt]()
### Deployment
![Image Alt]()
### POSTMAN
![Image Alt]()
## 🔗 Links
[![Github](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/kartiksb911)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kartik-bhardwaj-07b7282b7/)
  # *Thank You*

