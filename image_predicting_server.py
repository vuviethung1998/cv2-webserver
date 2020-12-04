from src.services.main_service import app
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from src.config.config import *

if __name__ == '__main__':
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = PRETRAINED_MODEL
    # set device to use cpu
    config['device'] = 'cpu'
    config['cnn']['pretrained']=False
    config['predictor']['beamsearch']=False

    detector = Predictor(config)

    app.run(host='0.0.0.0', port=5000, debug=True)
