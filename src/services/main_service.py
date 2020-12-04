from flask import Flask, request, jsonify
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from src.models.image_predictor import image_predictor
from src.config.config import *
import requests
import json
import cv2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

detector = None # init detector as global var 

@app.route('/init', methods=['POST'])
def init():
    global detector 
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = PRETRAINED_MODEL
    # set device to use cpu
    config['device'] = 'cpu'
    config['cnn']['pretrained']=False
    config['predictor']['beamsearch']=False

    detector = Predictor(config)
    return  jsonify({"result": 'init ok'})

@app.route('/uninit', methods=['POST'])
def uninit():
    global detector 
    del detector
    return  jsonify({"result": 'uninit ok'})


@app.route('/predict', methods=['POST'])
def image_predict():
    data = request.files['file']
    res = image_predictor(data,detector)
    # print(type(res))
    # print(res)
    return  jsonify({"result": res})

