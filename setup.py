# -*- coding: utf8 -*-

import platform
from setuptools import setup

reqs = ['requests==2.23.0', 'chardet==3.0.4']



if not platform.python_version()[:-2] < '2.7':
      reqs.append('ordereddict==1.1')

setup(
      name='tsutil',
      version='0.1.7.2',
      py_modules=['tsutil.util', 'tsutil.daemonize', 'tsutil.sync', 'tsutil.sequence'],
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

