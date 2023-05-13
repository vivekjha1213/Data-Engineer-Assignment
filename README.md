# Data-Engineer-Assignment


------------------------------------------XXXXXXXXXX------------------------------------------XXXXXXXXXX---------------------------

Technical Task
● Imagine you are working as a Data Scientist for an Online Wine Shop named “The Wine Land” (Dream come true??).
● As the name suggests, the online store specializes in selling different varieties of wines. ● Wines and its allied activities are niches. Having said that, the online store receives a decent amount of traffic and reviews from its users.
● Your boss is hoping to leverage the “reviews” data and draw actionable insights from it.
What is Expected?
● The directives from your boss are -
○ To derive the top 5 actionable Insights from the Data.
○ To build a predictive model for predicting the wine “variety”.
○ To build an API for serving predictions. Feel free to define the I/O contract.
Outcome
● Submit a one-page word/pdf document highlighting the actionable insights from the
analysis. Feel free to add code snippets wherever necessary.
● Clearly state the assumptions made (if any).
● Submit the source code used for building models in a zip or share the link to the GitHub
repository.
About the Dataset -
● The dataset can be downloaded from - https://drive.google.com/file/d/1ra9lwNjK9G8Ns0bAfzipD0u3Xwii5hc0/view
● The Data Description is as follows -
○ user_name - user_name of the reviewer
○ country -The country that the wine is from.
○ review_title - The title of the wine review, which often contains the vintage.
○ review_description - A verbose review of the wine.
○ designation - The vineyard within the winery where the grapes that made the wine are from.
○ points - ratings given by the user. The ratings are between 0 -100.
○ price - The cost for a bottle of the wine
○ province - The province or state that the wine is from.
○ region_1 - The wine-growing area in a province or state (ie Napa).
○ region_2 - Sometimes there are more specific regions specified within a wine-growing area (ie Rutherford inside the Napa Valley), but this value can sometimes be blank.
○ winery - The winery that made the wine
○ variety - The type of grapes used to make the wine. Dependent variable for task 2 of the assignment.

------------------------------------------XXXXXXXXXX------------------------------------------XXXXXXXXXX---------------------------


To run a Flask app, you can follow these general steps:

1. Set up a virtual environment for your Flask app (optional but recommended).
2. Install Flask and any other dependencies needed for your app.
3. Create a Python file for your Flask app and define your Flask routes and views.
4. Run the Flask app using the Flask command line interface.

Here's an example of how to run a basic Flask app:

1. Set up a virtual environment (optional):

```
python3 -m venv myenv
source myenv/bin/activate
```

2. Install Flask:

```
pip install Flask
```

3. Create a Python file for your Flask app (e.g. `app.py`) and define your routes and views:

```python
import csv
from flask import Flask, jsonify

app = Flask(__name__)
def read_csv_file():
    with open('OSX_DS_assignment.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader)
        return rows

@app.route('/wines', methods=['GET'])
def wine_data():
    data = read_csv_file()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```

4. Run the Flask app using the Flask command line interface:

```
export FLASK_APP=app.py
flask run
```

Your Flask app should now be running on `http://localhost:5000/`.


### Dependencies
The application requires the following dependencies:
- Flask
- scikit-learn
- joblib
- numpy

### Running the Application

To run the application, run the following command:

```
python3 app.py
flask run
```

This Application will run on `http://localhost:5000/`



------------------------------------------XXXXXXXXXX------------------------------------------XXXXXXXXXX---------------------------


This is a Flask web application that predicts wine varieties based on the given points and price.
where The model is trained using a Random Forest Classifier.

For POST, you can use the following curl command:

curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"points": 90, "price": 20}'

This sends a JSON object with the wine data (points and price) in the request body to the /predict endpoint of the Flask app running locally on port 5000. The response will be a JSON object containing the predicted wine variety.



For GET, you can use the following curl command:


curl http://127.0.0.1:5000/wines
This will return all the data in the CSV file after removing unnecessary features.


### URLs

- `/wines`: GET request that returns all data in the CSV file, with some unnecessary features removed.
- `/predict`: POST request that takes in JSON data with "points" and "price" features, and returns a JSON response with the predicted wine variety.

### Request Body

- `/predict`: JSON data with the following features:
  - `points`: integer (required)
  - `price`: integer (required)

### Example Request Body

```
{
    "points": 85,
    "price": 30
}
```

### Example Response

- `/predict`: JSON response with the following feature:
  - `prediction`: string
```
{
    "prediction": "Chardonnay"
}
```

### Training the Model

The model is trained using the `train_model()` function, which loads the data from the CSV file, preprocesses it, splits it into training and testing sets, trains a Random Forest Classifier, makes predictions on the test set, and calculates the accuracy of the model.

The trained model is saved to disk using the `joblib` library and loaded using the `LoadModel()` function.

### Preprocessing the Data

The `preprocess_data()` function removes some unnecessary features, and converts the "points" and "price" features to integers.







