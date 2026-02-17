from flask import Flask
from config import Config
from routers.home.main_home import main_home_bpp

app = Flask(__name__, template_folder='../../src/frontend/templates', static_folder='../../src/frontend/static')
app.config.from_object(Config)

app.register_blueprint(main_home_bpp)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])