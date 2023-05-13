# Data-Engineer-Assignment


This is a Flask web application that predicts wine varieties based on the given points and price. The model is trained using a Random Forest Classifier.

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

### Dependencies

This application requires the following dependencies:
- Flask
- scikit-learn
- joblib
- numpy

### Running the Application

To run the application, run the following command:

```
python app.py
```

The application will run on `http://localhost:5000/`.
