# code: https://viblo.asia/p/nhan-dang-tieng-viet-cung-voi-transformer-ocr-Qpmlejjm5rd
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter

config = Cfg.load_config_from_name('vgg_transformer')
# load pretrained weight
# param={
#     'num_workers':4
# }
# params = {
#     'print_every':200,
#     'valid_every':15*200,
#     'iters':20000,
#     'checkpoint':'data/checkpoint/transformerocr_checkpoint.pth',
#     'export':'data/pretrained_model/transformerocr.pth',
#     'metrics': 10000,
#     'batch_size':64,
# }
#
# params_opt = {
#     'init_lr': 0.01,
#     'n_warmup_steps': 400
# }
# config['dataloader'].update(param)
# config['trainer'].update(params)
# config['device'] = 'cuda:0'
config['weights'] = 'data/pretrained_model/transformerocr.pth'

# set device to use cpu
config['device'] = 'cpu'
config['cnn']['pretrained']=False
config['predictor']['beamsearch']=False


if __name__=="__main__":
    detector = Predictor(config)
    img = Image.open('data/img/test8.jpg')
    img = np.array(img)
    # img = img[:100,0:170,:]
    img = Image.fromarray(img)
    import matplotlib.pyplot as plt
    # img = img.crop((0,850,500,1100))
    plt.imshow(img)
    # # predict


    result = detector.predict(img)
    print(result)