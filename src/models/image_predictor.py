from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import numpy as np
from PIL import Image
from src.config.config import *

# PRETRAINED_MODEL = "data/pretrained_model/transformerocr.pth"
# test_img = 'data/img/test8.jpg'

def image_predictor(img_file,detector):
    img = Image.open(img_file)
    img = np.array(img)
    img = Image.fromarray(img)

    result = detector.predict(img)
    return  result

if __name__=="__main__":
    # image_predictor()
    res = image_predictor(test_img)
    print(res)