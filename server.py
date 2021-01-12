from flask import Flask , render_template


app = Flask(__name__, static_url_path='', static_folder='static-art', template_folder='template-art')


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/schedule.html')
def schedule():
    return render_template('schedule.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')


@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(port=3000)
