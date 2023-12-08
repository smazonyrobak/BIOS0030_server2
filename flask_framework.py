# flask_framework.py
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("http://localhost:8866/voila/render/Spatial_Test/Spatial_Test.ipynb")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
