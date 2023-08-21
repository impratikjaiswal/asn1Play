import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from werkzeug.exceptions import abort

from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.constants_config import ConfigConst

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/asn1Play', methods=('GET', 'POST'))
def asn1Play():
    output_data = ''
    version = f'v{ConfigConst.TOOL_VERSION}'
    if request.method == 'POST':
        raw_data = request.form['raw_data']
        input_format = request.form['input_format']
        output_format = request.form['output_format']
        asn1_element = request.form['asn1_element']
        remarks_list = request.form['remarks_list']

        # if not raw_data:
        #     flash('raw_data is required!')
        # if not input_format:
        #     flash('input_format is required!')
        # if not output_format:
        #     flash('output_format is required!')
        # else:
        #     return redirect(url_for('asn1Play'))
        data_type = DataTypeMaster()
        data_type.set_data_pool(data_pool=request.form.to_dict())
        data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
        return render_template('asn1Play.html', version=version, output_data=data_type.get_output_data())
    if request.method == 'GET':
        return render_template('asn1Play.html', version=version)
    return render_template('asn1Play.html', version=version)


@app.route('/tlvPlay', methods=('GET', 'POST'))
def tlvPlay():
    return render_template('wip.html', page='tlvPlay', git_end_point='tlvPlay')


@app.route('/excelPlay', methods=('GET', 'POST'))
def excelPlay():
    return render_template('wip.html', page='excelPlay', git_end_point='excelPlay')


@app.route('/sponsorship', methods=('GET', 'POST'))
def sponsorship():
    return render_template('wip.html', page='sponsorship')


@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('aboutus.html')


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
    if request.method == 'GET':
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('testimonials.html', posts=posts)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        publisher = request.form['publisher']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)',
                         (title, content, publisher))
            conn.commit()
            conn.close()
            return redirect(url_for('testimonials'))
    return render_template('testimonials.html')
