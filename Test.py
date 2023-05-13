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

#This code is for get all the data present in csv.file ..........................