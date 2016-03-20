import logging
import os

from flask import Flask, render_template, request, redirect, flash, url_for

from filters import datetimeformat
from leafs.fs import FileSystem, DuplicatedFileError

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.secret_key = '9E5AFB33C4F470FA442544F2483FC69D'
app.jinja_env.filters['datetime'] = datetimeformat

CONFIG = {
    'mongo': {
        'host': 'localhost',
        'port': 27017,
        'name': 'leafs',
        'collection': 'files',
    }
}

fs = FileSystem(config=CONFIG)


@app.route('/')
def index():
    path = request.args.get('path') or '/'
    fs.cwd = path
    logger.debug('Get list of %s', fs.cwd)
    filelist = []
    for file in fs.listdir(path=path):
        file['path'] = os.path.join(file['path'], file['name'])
        filelist.append(file)

    return render_template('index.html', current_path=path, filelist=filelist)


@app.route('/add/file/')
def add_file():
    path = request.args.get('path') or fs.cwd
    filename = request.args.get('name')

    try:
        fs.mkfile(name=filename, path=path)
        flash('File <strong>%s</strong> successfully created.' % filename, category='success')
    except DuplicatedFileError as e:
        logger.debug(e.message)
        flash('Duplicated Name <strong>%s.</strong>' % filename, category='danger')
    except Exception as e:
        logger.error(e)
        flash('Could not create file <strong>%s.</strong>' % filename, category='danger')

    return redirect(url_for('index', path=path))


@app.route('/add/folder/')
def add_folder():
    path = request.args.get('path') or fs.cwd
    filename = request.args.get('name')
    try:
        fs.mkdir(name=filename, path=path)
        flash('File <strong>%s</strong> successfully created.' % filename, category='success')
    except DuplicatedFileError as e:
        logger.debug(e.message)
        flash('Duplicated Name <strong>%s.</strong>' % filename, category='danger')
    except Exception as e:
        logger.error(e)
        flash('Could not create file <strong>%s.</strong>' % filename, category='danger')

    return redirect(url_for('index', path=path))


@app.route('/metadata')
def metadata():
    path = request.args.get('path')
    logger.debug('Get metadata for object: %s' % path)
    # path = request.args.get('path')
    if not path:
        return render_template('metadata.html')

    metadata = fs.info(path)
    print path
    print metadata
    return render_template('metadata.html', metadata=metadata)


if __name__ == '__main__':
    app.run(debug=True)
