from flask import Flask , render_template
from models import scholuder_model
import datetime
app = Flask(__name__, static_url_path='', static_folder='static-art', template_folder='template-art')

student_name = 'Shira Levi'

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/schedule.html')
def schedule():
    student_class = scholuder_model.get_class_by_student(student_name)
    data = scholuder_model.get_week_schedule_by_class(student_class)
    day = datetime.datetime.today().weekday()
    hour = datetime.datetime.now().hour
    date = datetime.datetime.today().strftime('%A - %B %d:')
    return render_template('schedule.html', week_schedule= data, day=day + 1, hour=hour,date=date)


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
