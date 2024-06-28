# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:59:35 2018

@author: Balasubramaniam
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    print('Content-Type: text/plain')
    return "Hello from FastCGI via IIS!"
if __name__ == "__main__":
    app.run()