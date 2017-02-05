import os
import sys

pwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(pwd)
new_path = pwd.strip(project)
activate_this = os.path.join(new_path, 'beak')
sys.path.append(activate_this)

from beak import app

def before_feature(context, feature):
    app.config['SERVER_NAME'] = '127.0.0.1:5001'
    context.client = app.test_client()
