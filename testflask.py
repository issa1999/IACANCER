from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/",methods=["POST"])
def traitement():
    #traitement
    # data = request.files.getlist("images")
    # for image in data:
    #     image.save(image.filename)
    x =[{"type":"skin cancer","severity":"benign"},{"type":"heart cancer","severity":"malignant"}]
    
    return jsonify(x)


app.run(debug=True)