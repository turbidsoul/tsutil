# -*- coding: utf8 -*-

import platform
from setuptools import setup

reqs = ['requests==2.23.0']

setup(
      name='tsutil',
      version='0.1.8.1',
      py_modules=['tsutil.util', 'tsutil.daemonize', 'tsutil.sync', 'tsutil.sequence', 'tsutil.http_server'],
      author='Turbidsoul Chen',
      author_email='sccn.sq+py@gmail.com',
      url='http://github.com/turbidsoul/tsutil',
      description='my python tool module',
      license='MIT',
      install_requires=reqs,
      package_dir={'':'.'},
      include_package_data=True,
      package_data = {'require': ['*.txt']}
)

