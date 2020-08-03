# flask_blog/views.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    """ ログインしていない時の処理 session['logged_in'] = Falseの場合 """
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ ログイン時の処理 """
    if request.method == 'POST':
        if request.form ['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            """ session['logged_in'] = Trueによってログイン状態の確認 """
            session['logged_in'] = True
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """ ログアウト後にsession情報を削除 """
    session.pop('logged_in', None)
    return redirect('/')
