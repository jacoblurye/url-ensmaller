from app import app
from app.models import URLMap
from app.forms import URLForm
from flask import render_template, redirect, url_for, flash, jsonify
import validators 

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        if not validators.url(form.url.data):
            return jsonify(success=False)
        alias = URLMap.insert(form.url.data)
        return jsonify(success=True, alias=alias)
    return render_template('index.html', form=form)

@app.route('/<alias>', methods=['GET'])
def lookup(alias):
    long_url = URLMap.find_url(alias)
    if long_url:
        return redirect(long_url)
    return 'Error – URL not found'