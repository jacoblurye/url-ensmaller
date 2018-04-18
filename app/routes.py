from app import app
from app.models import URLMap
from app.forms import URLForm
from flask import render_template, redirect, url_for, abort

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        # Add URL mapping to cache/DB
        # TODO: validate form.inURL.data -- make a request?
        if not URLMap.insert(form.outURL.data, form.inURL.data):
            # TODO: flash the user that that name is taken
            pass
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/<key>', methods=['GET'])
def lookup(key):
    long_url = URLMap.find(key)
    if long_url:
        return redirect(long_url)
    abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return '404 – not found', 404
