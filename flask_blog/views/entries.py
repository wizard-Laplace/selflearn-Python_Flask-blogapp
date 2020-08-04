# flask_blog/views/entries.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog.models.entries import Entry
from flask_blog import db

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

@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )

    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))
