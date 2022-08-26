from flask import Flask, request, jsonify
from PIL import Image

from business.image_classification import classify
from dao.mongo_dao import MongoDAO, get_client

app = Flask("")

db = get_client("mongo")
dao = MongoDAO(db)


@app.route("/image/predict", methods=["POST"])
def test():
    file = request.files['file']

    img = Image.open(file)
    img = img.convert('RGB')
    img = img.resize((224,224), Image.NEAREST)

    clf = classify(img)

    return jsonify(dict(prediction=clf))

@app.route("/insert", methods=["POST"])
def insert():
    j = request.json
    print(j)
    coll = j.get('args').get('collection')
    row = j["value"]
    ret = dao.insert(coll,row)
    return jsonify(dict(msg=ret))

@app.route("/search", methods=["POST"])
def search():
    j = request.json
    print(j)
    coll = j.get('args').get('collection')
    filter = j["value"]
    ret = list(dao.search(coll, filter))
    return jsonify(ret)

@app.route("/delete", methods=["POST"])
def delete():
    j = request.json
    print(j)
    coll = j.get('args').get('collection')
    filter = j["value"]
    ret = dao.delete(coll, filter)
    return jsonify(dict(msg=ret))


app.run("0.0.0.0", 8080)
