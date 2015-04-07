from setuptools import setup

VERSION = '0.0.1'

setup(
    name='FacebookWall',
    version=VERSION,
    description='Building a FacebookWall-like App',
    author='Vincent Montesclaros',
    author_email='montesclaros.vince@gmail.com',

    packages=['posts', ],
    package_dir={'': 'src/FacebookWall'},

    install_requires=[
        'django == 1.6.8',
    ]
)
