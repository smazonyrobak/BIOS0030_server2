import os
from flask import Flask, redirect

app = Flask(__name__)

root_url = 'https://uclbios-c7accae8eb34.herokuapp.com/'

# Use os.environ.get to access the PORT environment variable provided by Heroku
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    return redirect(f'{root_url}voila/render/Spatial_Test/Spatial_Test.ipynb')

if __name__ == '__main__':
    # Bind the app to the dynamically assigned port
    app.run(host='0.0.0.0', port=port)
