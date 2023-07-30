import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from werkzeug.exceptions import abort

from src.main.data_type.data_type_master import DataTypeMaster
from src.main.helper.data import Data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/asn1Play', methods=('GET', 'POST'))
def asn1Play():
    output_data = ''
    if request.method == 'POST':
        raw_data = request.form['raw_data']
        input_format = request.form['input_format']
        output_format = request.form['output_format']
        asn1_element = request.form['asn1_element']
        remarks_list = request.form['remarks_list']

        if not raw_data:
            flash('raw_data is required!')
        if not input_format:
            flash('input_format is required!')
        if not output_format:
            flash('output_format is required!')
        # else:
        #     return redirect(url_for('asn1Play'))
        data_type = DataTypeMaster()
        data_type.set_data_pool(data_pool=[
            Data(raw_data=raw_data, input_format=input_format, output_format=output_format, asn1_element=asn1_element,
                 remarks_list=remarks_list)])
        data_type.parse(PhErrorHandlingModes.CONTINUE_ON_ERROR)
        output_data = data_type.meta_data_pool[0]
    return render_template('asn1Play.html', output_data=output_data)


@app.route('/tlvPlay')
def tlvPlay():
    pass


@app.route('/excelPlay')
def excelPlay():
    pass


def get_db_connection():
    # conn = sqlite3.connect(r'database.db')
    path = os.sep.join([os.path.dirname(os.path.realpath(__file__)), 'db', 'database.db'])
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/testimonials', methods=('GET', 'POST'))
def testimonials():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user = request.form['publisher']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('testimonials.html')
