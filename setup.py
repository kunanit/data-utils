from setuptools import setup

setup(
    name='data-utils',
    version='0.1',
    py_modules=['data_utils'],
    install_requires=[
        's3fs',
        'sqlalchemy',
        'pandas',
    ]
)
