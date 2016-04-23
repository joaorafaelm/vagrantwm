# coding=utf-8
""" Vagrant wrapper """
import json
from os import environ
from subprocess import Popen, PIPE


class Vagrant(object):
    """
        Base class
    """
    __machines = []
    __version = 0
    __selected_machine = None

    def __init__(
            self,
            vm_id: str = None,
            vagrant_file: str = None,
            vagrant_bin: str = None,
            stdout=PIPE,
            stderr=PIPE
    ):
        self.__vagrant_exec = vagrant_bin
        self.__vagrant_machines_state_file = vagrant_file
        self.__stdout = stdout
        self.__stdoerr = stderr
        self.machines = vagrant_file
        self.machine = vm_id

    def __exec_call(self, args: list, force=False):
        if self.__selected_machine:
            args = args + [self.__selected_machine['name']]
            if force:
                args = args + ['--force']
            command = Popen(
                args,
                shell=True,
                cwd=self.__selected_machine.get('vagrantfile_path'),
                env=environ.copy(),
                executable=self.__vagrant_exec,
                stdout=self.__stdout,
                stderr=self.__stdoerr
            )
            output, err = command.communicate()
            return_code = command.returncode

            # updates machines states by re-reading state file
            if return_code == 0:
                self.machines = self.__vagrant_machines_state_file

            return return_code, output, err
        else:
            raise Exception("No machine selected")

    @property
    def version(self) -> int:
        """ Vagrant major version """
        return self.__version

    @property
    def machines(self) -> list:
        """
            Return list of machines
            :return: List of objects with details
        """
        machines = []
        for machine in self.__machines:
            self.__machines[machine].update({'id': machine})
            machines.append(self.__machines[machine])

        return machines

    @machines.setter
    def machines(self, vagrant_file: str) -> None:

        with open(vagrant_file) as file:
            data = json.load(file)
            self.__machines = data.get('machines', [])
            self.__version = data.get('version', 0)
            file.close()

        # updates selected machine details, if there is one
        if self.__selected_machine:
            self.machine = self.__selected_machine.get('id')

    @property
    def machine(self) -> dict:
        """ Selected machine """
        return self.__selected_machine

    @machine.setter
    def machine(self, machine_id: str) -> None:
        self.__selected_machine = self.__machines.get(machine_id, None)
        if self.__selected_machine:
            self.__selected_machine.update({'id': machine_id})

    def get(self, machine_id: str):
        """
        :param machine_id: machine hash identification
        :return: machine details
        """
        self.machine = machine_id
        return self

    def up(self) -> (int, bytes, bytes):
        """
            Turn machine on
        :return: return_code 0 = Success, 1 = Failed
        :return: stdout
        :return: stderr
        """
        return self.__exec_call(['up'])

    def halt(self, force: bool = True) -> (int, bytes, bytes):
        """
            Turn machine off
        :param force - ignores any TTY input
        :return: return_code - 0 = Success, 1 = Failed
        :return: stdout
        :return: stderr
        """
        return self.__exec_call(['halt'], force=force)

    def suspend(self) -> (int, bytes, bytes):
        """
            Suspends the machine
        :return: return_code - 0 = Success, 1 = Failed
        :return: stdout
        :return: stderr
        """
        return self.__exec_call(['suspend'])

    def destroy(self) -> (int, bytes, bytes):
        """
            Destroys machine
        :return: return_code - 0 = Success, 1 = Failed
        :return: stdout
        :return: stderr
        """
        return self.__exec_call(['destroy'], force=True)

    @staticmethod
    def init(self):
        """ Creates new machine"""
        pass
