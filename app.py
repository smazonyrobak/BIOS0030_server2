from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the Voilà-rendered notebook
    return redirect("https://uclbios-c7accae8eb34.herokuapp.com/voila/render/Spatial_Test/Spatial_Test.ipynb")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
