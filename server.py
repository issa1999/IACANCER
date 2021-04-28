from flask import Flask,jsonify,request
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import load_model
import os
import numpy as np
from flask_cors import CORS

BASEDIR = "/".join(os.path.abspath(__file__).split("/")[:-1])
app = Flask(__name__)
CORS(app)

typeCancerModel = load_model(os.path.join(BASEDIR,"models/modelTypeClassification.h5"))
severityCancerModel = load_model(os.path.join(BASEDIR,"models/modelSeverityClassification.h5"))
print("models loaded")

types = ['melanoma',
 'squamous cell carcinoma',
 'actinic keratosis',
 'dermatofibroma',
 'pigmented benign keratosis',
 'seborrheic keratosis',
 'basal cell carcinoma',
 'vascular lesion',
 'nevus']

severities = ["benign","malignant"]

    

@app.route("/",methods=["POST"])
def cancerClassification():
    results = []
    images = request.files.getlist("images")
    for image in images:
        image.save(image.filename)
        x = load_img(image.filename,target_size=(224,224))
        x = np.expand_dims(img_to_array(x),0)
        #models to predict
        typee = typeCancerModel.predict(x)
        severity = severityCancerModel.predict(x)
        percentage = round(np.max(severity)*100,2)
        print(percentage)
        typee = types[np.argmax(typee)]
        severity = severities[np.argmax(severity)]
        results.append({"type":typee,"severity":severity,"percent":percentage})
        os.remove(image.filename)


    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
