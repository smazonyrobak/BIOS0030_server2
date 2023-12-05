from flask import Flask, redirect
import voila.app
import os

#Flask web framework
os.chdir(os.path.join(os.getcwd(), '..'))

uclbiosapp = Flask(__name__)

# Voila configuration
voila_app.initialize(argv=[
    '--no-browser',            # Prevents Voilà from opening a browser automatically
    '--port=8866',             # Sets Voilà to run on port 8866 to avoid conflict with Flask
    '--autoreload=False',      # Sets whether Voilà should autoreload; set to True if needed
    '--show_tracebacks=False'  # Hides tracebacks in the output
])
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
