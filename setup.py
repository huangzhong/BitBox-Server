import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='bitbox-server',
    version='0.0.4',
    author='Alex Gajewski, Wanqi Zhu, Ashwin Aggarwal',
    author_email='agajews@gmail.com, 1213.ghs@gmail.com, aaggarw99@gmail.com',
    description=('A continuous hosting system for rapid prototyping '
                 'and monitoring of bitcoin trading algorithms.'),
    license='MIT',
    url='http://github.com/CoinTK',
    packages=['bitbox_server'],
    long_description=read('README.md'),
    install_requires=['numpy', 'pprint', 'flask', 'flask-restful', 'pymongo',
                      'conitk'],
    scripts=['scripts/bitbox']
)
