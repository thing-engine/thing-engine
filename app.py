import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
@app.route('/api/', methods=['POST'])
def makecalc():
	data = request.get_json()
	prediction = np.array2string(model.predict(data))

	return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)