from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, request
from sklearn import datasets
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

CORS(app)

digits = datasets.load_digits()
from sklearn.cluster import KMeans
model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

class ML(Resource):
    def get(self):
        abort(404, message="Sorry, i only do post requests at the moment.")

    def post(self):
        new_sample = request.json
        # print(new_sample)
        if new_sample is None:
            abort(404, message="Sorry, it does not look like you send me any data i could work with. Do send me Data as JSON please.")
        new_samples = new_sample["data"]
        # print(new_samples)
        if isinstance(new_samples, str):
            new_samples = eval(new_samples)
        # new_samples = request.args.get('array')
        # new_samples = eval(new_samples)
        # print(new_samples)
        new_labels = model.predict(new_samples)
        new_string = ""
        for i in range(len(new_labels)):
            if new_labels[i] == 0:
                new_string += "0"
            elif new_labels[i] == 1:
                new_string += "9"
            elif new_labels[i] == 2:
                new_string += "2"
            elif new_labels[i] == 3:
                new_string += "1"
            elif new_labels[i] == 4:
                new_string += "6"
            elif new_labels[i] == 5:
                new_string += "8"
            elif new_labels[i] == 6:
                new_string += "4"
            elif new_labels[i] == 7:
                new_string += "5"
            elif new_labels[i] == 8:
                new_string += "7"
            elif new_labels[i] == 9:
                new_string += "3"
        return {"data": new_string}


api.add_resource(ML, "/")

if __name__ == '__main__':
    app.run()
