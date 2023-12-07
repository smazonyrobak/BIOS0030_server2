from flask import Flask, Response
import os
from voila.app import Voila

uclbiosapp = Flask(__name__)
root_dir = os.getcwd()
os.chdir(root_dir)

def run_and_display_notebook(file):
    notebook_path = (f'{file}/{file}.ipynb')
    voila_readout = Voila(notebook_path = notebook_path)
    render_notebook = voila_readout.render_notebook()
    return Response(render_notebook, content_type='text/html')

@uclbiosapp.route('/')
def main_menu():
    return run_and_display_notebook('All_tests_launcher')

@uclbiosapp.route('/ANS_Test')
def ANS_test():
    return run_and_display_notebook('ANS_Test')

@uclbiosapp.route('/Maths_Test')
def Maths_Test():
    return run_and_display_notebook('Maths_Test')

@uclbiosapp.route('/Memory_Test')
def Memory_Test():
    return run_and_display_notebook('Memory_Test')
