# coding=utf-8
""" Base API router """

from flask import Flask, render_template
from flask_restful import Api
from vagrantwm.resources.machines import Machines

app = Flask(__name__)
api = Api(app)


api.add_resource(
    Machines,
    '/machines/',
    '/machine/<string:machine_id>',
    endpoint="machines"
)


@app.route('/')
def index():
    """" Index """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
