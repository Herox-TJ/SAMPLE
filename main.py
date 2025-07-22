from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

@app.route('/timetable/day')
def timetable_day():
    return render_template('timetable-day.html')

@app.route('/timetable/grade')
def timetable_grade():
    return render_template('timetable-grade.html')

@app.route('/timetable/coach')
def timetable_coach():
    return render_template('timetable-coach.html')

if __name__ == '__main__':
    app.run(debug=True)
