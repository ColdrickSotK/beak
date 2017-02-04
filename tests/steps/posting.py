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

"""Test implementations for the /posts/ endpoint."""

import subprocess

from behave import *
import requests


@given('a beak server')
def step_impl(context):
    context.endpoint = 'http://localhost:8080/posts/'
    context.server = subprocess.Popen(['python', 'beak/app.py'])


@when('the user tries to create a valid post')
def step_impl(context):
    post = {
        "title": "My Great Post",
        "content": "This is a fascinating tale.",
        "tags": "foo bar baz",
        "category": "testing",
        "author": "Mr Boop"
    }
    context.response = requests.post(context.endpoint, data=post)


@when('the user tries to create a post with no title')
def step_impl(context):
    post = {
        "content": "This is a fascinating tale.",
        "tags": "foo bar baz",
        "category": "testing",
        "author": "Mr Boop"
    }
    context.response = requests.post(context.endpoint, data=post)


@then('the post is created')
def step_impl(context):
    assert context.response.status_code == 200


@then('the response is a {code} error')
def step_impl(context, code):
    assert context.response.status_code == code
