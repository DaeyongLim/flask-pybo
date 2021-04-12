from logging.config import dictConfig
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'%\xeb\x07\xd4f\x8a\xad\xf7\xec\x92F\xac\xa7Ax\x1e'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root':{
        'level':'INFO',
        'handlers':['file']
    }
})

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user = 'dbmasteruser',
    pw = 'data_base',
    url = 'ls-ffe2f27d734d1c77362cb38a6f5bd074d19f8b44.cktab70ijezv.ap-northeast-2.rds.amazonaws.com',
    db = 'flask_pybo')