from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:index_title>')
def each_index(index_title):
    return render_template(index_title)

