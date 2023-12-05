from flask import Flask, redirect
import voila.app
import os

#Flask web framework

uclbiosapp = Flask(__name__)

# Voila configuration
voila_app = voila.app.Voila()
voila_app.initialize(argv=[
    '--enable_nbextensions=True',
    #'--VoilaConfiguration.trust_notebooks=True'
])
os.chdir(os.path.join(os.getcwd(), '..'))
@uclbiosapp.route('/')
def index():
    return redirect('/voila/render/All_tests_launcher/All_tests_launcher.ipynb')

@uclbiosapp.route('/ANS_test')
def ans_test():
    return redirect('/voila/render/ANS_test/ANS_Test.ipynb')
@uclbiosapp.route('/Maths_test')
def maths_test():
    return redirect('/voila/render/All_tests_launcher/Maths_Test.ipynb')

@uclbiosapp.route('/Memory_Test')
def memory_test():
    return redirect('/voila/render/Memory_Test/Memory_Test.ipynb')

@uclbiosapp.route('/Spatial_Test')
def spatial_test():
    return redirect('/voila/render/Spatial_Test/Spatial_Test.ipynb')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uclbiosapp.run(host='0.0.0.0', port=port)
