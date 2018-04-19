from app import app
from app.models import URLMap
from app.forms import URLForm
from flask import render_template, redirect, url_for, flash, jsonify

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        # TODO: validate form.inURL.data
        if not URLMap.insert(form.alias.data, form.url.data):
            return jsonify(success=False)
        return jsonify(success=True, alias=form.alias.data})
    return render_template('index.html', form=form)

@app.route('/<key>', methods=['GET'])
def lookup(key):
    long_url = URLMap.findURL(key)
    if long_url:
        return redirect(long_url)
    return 'Error – URL not found'