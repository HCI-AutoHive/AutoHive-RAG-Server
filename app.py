from flask import Flask
from app.routes.chian_routes_faiss import chian_bp

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(chian_bp)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()