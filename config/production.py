from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite://{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'%\xeb\x07\xd4f\x8a\xad\xf7\xec\x92F\xac\xa7Ax\x1e'