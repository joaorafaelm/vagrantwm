# coding=utf-8
""" Runs flask server """
from vagrantwm import app
from vagrantwm.settings import DEBUG


def run_server():
    """ Runs dev server """
    app.debug = DEBUG
    app.run()

if __name__ == '__main__':
    run_server()
