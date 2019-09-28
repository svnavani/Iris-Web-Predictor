# Iris-Web-Predictor

The Iris Web Predictor serves as a web interface for the classic iris predicting machine learning algorithm. The web interface was built using the python backend Flask. I used bootstrap to make the page responsive. The data was taken from the form and sent to my backend using an AJAX call in my ml.js file. The data would be inputed into the web_iris.py file where a prediction would be returned to app.py. app.py sends that prediction back to the ml.js file and finally the prediction is updated in the HTML.

To predict the species of flower, I used a decision tree classifier.
