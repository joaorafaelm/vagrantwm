# coding=utf-8
""" Unit test for machines file parse """

import unittest
from utils.vagrant import Vagrant
from os.path import join, dirname

VAGRANT_MACHINES_STATE_FILE = join(dirname(__file__), 'sample_machine_file.json')
machines = Vagrant(vagrant_file=VAGRANT_MACHINES_STATE_FILE)


class TestFileParse(unittest.TestCase):
    machines = None

    def test_machines_load(self):
        self.assertEqual(type(machines.machines), list)

    def test_version(self):
        self.assertEqual(machines.version, 1)

    def test_machine_name(self):
        machine = machines.get('475df7124f3341ff8671f2edf784b2a9').machine
        self.assertEqual(machine.get('name'), 'vm1')
        self.assertEqual(machine.get('state'), 'poweroff')


if __name__ == '__main__':
    unittest.main()
