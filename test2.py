from flask import Flask
from api import blueprint as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1)

if __name__ == '__main__':
    app.run(debug=True)

