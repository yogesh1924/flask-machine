import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
app=Flask(__name__)

loaded_pickle_model = pickle.load(open("firstdep.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    float_features= [float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction=loaded_pickle_model.predict(features)
    
    return render_template("index.html", prediction_text= "heart_diseasse satge is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug = False)