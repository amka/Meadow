from setuptools import setup

setup(
    name='Meadow',
    version='0.1',
    packages=['meadow'],
    url='https://github.com/amka/meadow/',
    license='BSD',
    author='Andrey Maksimov',
    author_email='meamka@ya.ru',
    description='Python virtual file system sample app',
    long_description=__doc__,
    install_requires=[
        'flask==0.10.1',
    ],
)
