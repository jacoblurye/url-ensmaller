from app import app
from app.models import URLMap
from app.forms import URLForm
from flask import render_template, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        # TODO: validate form.inURL.data
        if not URLMap.insert(form.alias.data, form.inURL.data):
            flash("Alias %s is taken. Please choose another!" % form.alias.data)
            return redirect(url_for('index'))
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success', methods=['GET'])
def success():
    return "Success!"

@app.route('/<key>', methods=['GET'])
def lookup(key):
    long_url = URLMap.findURL(key, setcache=True)
    if long_url:
        return redirect(long_url)
    return 'Error – URL not found'