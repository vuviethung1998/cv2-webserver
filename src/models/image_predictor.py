from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import numpy as np
from PIL import Image
from src.config.config import *

# PRETRAINED_MODEL = "data/pretrained_model/transformerocr.pth"
test_img = 'data/img/test8.jpg'

def image_predictor(img_file):
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = PRETRAINED_MODEL
    # set device to use cpu
    config['device'] = 'cpu'
    config['cnn']['pretrained']=False
    config['predictor']['beamsearch']=False

    detector = Predictor(config)
    img = Image.open(img_file)
    img = np.array(img)
    img = Image.fromarray(img)

    result = detector.predict(img)
    return  result

if __name__=="__main__":
    # image_predictor()
    res = image_predictor(test_img)
    print(res)