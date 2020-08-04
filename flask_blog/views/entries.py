# flask_blog/views/entries.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog.models.entries import Entry

@app.route('/')
def show_entries():
    """ ログインしていない時の処理 session['logged_in'] = Falseの場合 """
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')

@app.route('/entries/new', methods=['GET'])
def new_entry():
    """ new_entryビューを追加 """
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')
