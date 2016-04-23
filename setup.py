# coding=utf-8
""" setup file"""

from setuptools import setup, find_packages

setup(
    name='vagrantwm',
    version='0.1.0',
    description='A vagrant web manager.',
    long_description='Vagrant web manager with rest and python API.',
    url='http://github.com/joaorafaelm/vagrantwm',
    license='MIT',
    author='João Rafael',
    author_email='joaoraf@me.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Flask==0.10.1',
        'Flask-RESTful==0.3.5',
        'python-dotenv==0.4.0',
        'pytest==2.9.1'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'run_server = vagrantwm.scripts:run_server'
        ]
    },
    package_data={
        'static': 'vagrantwm/static/*',
        'templates': 'vagrantwm/templates/*'
    },
    classifiers=[
        'Private :: Do Not Upload'
    ],
)
