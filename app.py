import csv
from flask import Flask, jsonify, request
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

app = Flask(__name__)

# the CSV file
CsV_file = "OSX_DS_assignment.csv"

def read_csv_file():
    rows = []
    with open(CsV_file, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rows.append(row)
    return rows


# this route is for Get all data->> in Csv.file...
@app.route("/wines", methods=["GET"])
def wine_data():
    data = read_csv_file()

    # THis is for Remove any unnecessary features
    features_to_remove = ["designation", "region_1", "region_2", "review_description"]
    for row in data:
        for feature in features_to_remove:
            row.pop(feature, None)

    return jsonify(data)


#  to preprocess the data before training the model
def preprocess_data(data):
    # Remove any unnecessary features
    features_to_remove = ["designation", "region_1", "region_2", "review_description"]
    for row in data:
        for feature in features_to_remove:
            row.pop(feature, None)

    # Convert points and price to integers
    for row in data:
        row["points"] = int(row["points"]) if row["points"] else 0
        row["price"] = int(float(row["price"])) if row["price"] else 0

    return data


# to train the predictive model
def train_model():
    # Load the data
    data = read_csv_file()

    # This is Preprocess the data
    data = preprocess_data(data)

    #  for Split the data into training and testing sets..............
    X = []
    y = []
    for row in data:
        X.append([row["points"], row["price"]])
        y.append(row["variety"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a Random Forest Classifier in dataset.......
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Make predictions on the test set.......
    y_pred = clf.predict(X_test)

    # for Calculate the accuracy of the model........
    accuracy = accuracy_score(y_test, y_pred)
    print("The Model accuracy: {:.2f}%".format(accuracy * 100))

    return clf


# to load the trained model from disk
def LoadModel():
    return joblib.load("model.joblib")

#  This is for  route to predict the wine variety
@app.route("/predict", methods=["POST"])
def predict_wine_variety():
    data = request.json
    model = LoadModel()
    data = preprocess_data([data])
    prediction = model.predict([[data[0]["points"], data[0]["price"]]])[0]
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)
