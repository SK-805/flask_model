from flask import Flask, jsonify, request
import pickle
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, 'model.pkl')

app = Flask(__name__)
model = pickle.load(open(model_path, 'rb'))
@app.route('/')
def home():
    return jsonify(data='Starting Point')

@app.route('/predict')
def predict():
    MedInc = request.args.get('MedInc')
    prediction = model.predict([[float(MedInc)]])
    return jsonify(prediction=str(prediction[0]))

if __name__ == '__main__':
    app.run(host='0.0.0.0')






