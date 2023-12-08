from flask import Flask, redirect

app = Flask(__name__)

root_url = 'https://uclbios-c7accae8eb34.herokuapp.com/'
@app.route('/')
def home():
    return redirect(f'{root_url}voila/render/Spatial_Test/Spatial_Test.ipynb')

if __name__ == '__main__':
    app.run()