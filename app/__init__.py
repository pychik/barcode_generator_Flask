from flask import Flask

from .config import Settings


app = Flask(__name__,
            static_url_path='/static')
app.secret_key = Settings.SECRET


from app import routes