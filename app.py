import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST','GET'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    return render_template('home.html',prediction_text='Salary = {}'.format(output))

if __name__=="__main__":
    app.run(debug=True)
