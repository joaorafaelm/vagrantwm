# coding=utf-8
""" Base model for Machine """

from flask_restful import Resource, abort
from vagrantwm.utils.vagrant import Vagrant
from vagrantwm.settings import VAGRANT_MACHINES_STATE_FILE, VAGRANT_BIN


class Machines(Resource):
    """
        Base
    """
    def __init__(self):
        parameters = {
            'vagrant_file': VAGRANT_MACHINES_STATE_FILE,
            'vagrant_bin': VAGRANT_BIN
        }
        self.__machine = Vagrant(**parameters)

    def get(self, machine_id: str = None):
        """
        :param machine_id: Optional
        :return: details object
        """
        if machine_id:
            machine = self.__machine.get(machine_id).machine
            return machine if machine else abort(404)
        else:
            return self.__machine.machines

    def put(self, machine_id: str = None):
        pass

    def delete(self, todo_id):
        pass
