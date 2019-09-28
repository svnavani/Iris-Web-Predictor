from flask import Flask, render_template, request, jsonify
import iris_web
import numpy as np

app = Flask(__name__)

clf = iris_web.initialize_clf()

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/process", methods=['GET', 'POST'])
def process():
	# get inputs
	sepalLength = request.form['sepalLength1']
	sepalWidth = request.form['sepalWidth']
	petalLength = request.form['petalLength']
	petalWidth = request.form['petalWidth']

	# make an np array of the inputs
	input_array = np.array([float(sepalLength), float(sepalWidth), float(petalLength), float(petalWidth)])
	
	# make a prediction
	prediction = iris_web.predict(clf, input_array)
	if prediction == 0: prediction = 'Iris Setosa' 
	if prediction == 1: prediction = 'Iris Versicolor' 
	if prediction == 2: prediction = 'Iris Virginica'

	# return the prediction
	return jsonify({'prediction': str(prediction)})

if __name__ == "__main__":
  app.run(debug=True)