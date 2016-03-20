# Meadow

Meadow is sample web app based on [Flask] and [Bootstrap] to show how to use [LeaFS].
It's allows you to create virtual folders and files, get listing directories and get metadata for objects.

### Installation

First you need to download sources on your computer and then do next (virtualenv optional):

    $ virtualenv /your/virtual/
    $ source /your/virtual/env/bin/activate
    $ (env) python setup.py install
    
After that you will be able to start local flask server with command:

    $ python Meadow.py
    
That command starts web server on http://127.0.0.1:5000 so you will may test LeaFS in your browser.


[Flask]: https://flask.pacoo.org/
[Bootstrap]: http://getbootstrap.com/
[LeaFS]: https://github.com/amka/LeaFS
