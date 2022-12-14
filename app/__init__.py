# project developed using git video
#!/usr/bin/env python3
# -*- coding utf8 -*-
""" Sample hello"""

from flask import Flask  # we imported flask class from flask module
import json

app = Flask(__name__)  # app is an instance


@app.route("/")
def index():  # our view funciton
    return "<h1>Hello Flask</h1>"  # return string


@app.get("/aboutme")
def about():  # our view funciton
    me = {
        "first_name": "Carlos Alberto",
        "last_name": "Lopez",
        "hobby": "travel",
    }
    return json.dumps(me)
