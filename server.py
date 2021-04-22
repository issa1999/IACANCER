from flask import Flask,jsonify,request
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import load_model
import os
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def initModels(classification=None,severity=None):
    global typeCancerModel
    global severityCancerModel
    typeCancerModel = load_model(classification)
    severityCancerModel = load_model(severity)

    

@app.route("/",methods=["POST"])
def cancerClassification():
    results = []
    images = request.files.getlist("images")
    for image in images:
        image.save(image.filename)
        x = load_img(image.filename,target_size=(224,224))
        x = np.expand_dims(img_to_array(x),0)
        #models to predict
        # typee = model.predict(x)
        # severity = model2.predict(x)
        results.append({"type":"typee","severity":"severity"})
        os.remove(image.filename)


    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
    # initModel("model.h5")
