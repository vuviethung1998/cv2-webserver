from flask import Flask, request, jsonify
from src.models.image_predictor import image_predictor
import requests
import json
import cv2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/home', methods=['POST'])
def home():
    data = request.files['file']
    return jsonify({"status":"ok"})


@app.route('/predict', methods=['POST'])
def image_predict():
    data = request.files['file']
    res = image_predictor(data)
    # print(type(res))
    # print(res)
    return  jsonify({"result": res})

