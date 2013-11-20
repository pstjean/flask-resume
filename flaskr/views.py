from flaskr import app, db
from flaskr.models import Entry, Asset, Timeline
from flask import Response, request, session, g, redirect, url_for, abort, render_template, flash, json
import datetime, time


# @app.before_request
# def before_request():
#     g.db = DB().connect_db()
#
#
# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()


@app.route('/')
def show_entries():
    entries = Entry.query.all()
    return render_template('show_entries.html', entries=entries)


@app.route('/_json_entries')
def json_entries():
    entries = dict()
    entries['timeline'] = {
        'headline': 'Work Experience',
        'type': 'default',
        'text': '<p>A timeline of work experiences</p>',
        'asset': {
            'media': '',
            'credit': 'Google Maps',
            'caption': 'Arlington, Virginia'
        }
    }
    entries['timeline']['date'] = list()
    for e in db.session.query(Entry):
        entry = dict({
            'startDate': e.startDate,
            'endDate': e.endDate,
            'headline': e.headline,
            'text': e.text
        })
        entry['asset'] = dict({
            'media': e.asset.media,
            'credit': e.asset.credit,
            'caption': e.asset.caption
        })
        entries['timeline']['date'].append(entry)
    js = json.dumps(entries)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

# @app.route('/_entry/<int:entryid>')
# def json_entry(entryid):
#     entry = Entry.query.filter_by(id=entryid).first()
#     js = json.dumps(jsonEntry)
#     if entry:
#         resp = Response(js, status=200, mimetype='application/json')
#     else:
#         resp = Response(None, status=404)
#     return resp


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    asset = Asset(request.form['media'],
                  request.form['credit'],
                  request.form['caption'])
    entry = Entry(request.form['headline'],
                  request.form['startDate'],
                  request.form['endDate'],
                  request.form['text'],
                  asset)
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
