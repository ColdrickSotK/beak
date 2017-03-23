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

import json
import os
import time

from flask import Flask
from flask import abort
from flask import render_template
from flask import request


app = Flask(__name__)


def write_metadata(post, orig_date=None):
    post.write('Title: %s\n' % request.form['title'])

    if orig_date is None:
        post.write('Date: %s\n' % time.strftime('%Y-%m-%d %H:%M'))
    else:
        post.write('Date: %s\n' % orig_date)
    post.write('Modified: %s\n' % time.strftime('%Y-%m-%d %H:%M'))

    if request.form.get('category'):
        post.write('Category: %s\n' % request.form['category'])
    else:
        post.write('Category: Misc\n')

    post.write('Tags: %s\n' % request.form['tags'])
    post.write('Authors: %s\n' % request.form['author'])

    if request.form.get('filename'):
        post.write('Slug: %s\n' % request.form['filename'])
    if request.form.get('summary'):
        post.write('Summary: %s\n' % request.form['summary'])


def add_post_from_request():
    post_dir = os.path.join('posts', time.strftime('%Y-%m-%d'))
    if not os.path.exists(post_dir):
        os.mkdir(post_dir)

    post_path = os.path.join(
        post_dir, request.form.get('filename', 'post') + '.md')

    orig_date = None
    if os.path.exists(post_path):
        with open(post_path, 'r') as post:
            for line in post.readlines():
                if line.startswith('Date: '):
                    orig_date = line[6:].strip()
                    break

    with open(post_path, 'w') as post:
        write_metadata(post, orig_date)
        post.write('\n%s' % request.form['content'])


def parse_post(raw):
    metadata, content = raw.split('\n\n', 1)
    metadata = {entry.split(':')[0].lower(): entry.split(': ')[1]
                for entry in metadata.split('\n')}
    return {'metadata': metadata, 'content': content}


@app.route('/posts/<slug>')
def get_post(slug):
    if not slug.endswith('.md'):
        slug += '.md'
    path = ''
    for root, dirs, files in os.walk('posts/'):
        if slug in files:
            path = os.path.join(root, slug)
            break
    if not path:
        abort(404)

    with open(path, 'r') as f:
        return json.dumps(parse_post(f.read()))


@app.route('/posts/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        add_post_from_request()
    return render_template('create.html')
