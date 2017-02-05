# Copyright 2017 Adam Coldrick
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Beak flask app for serving the API"""

import os

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/posts/create')
def new_post():
    return render_template('create.html')
