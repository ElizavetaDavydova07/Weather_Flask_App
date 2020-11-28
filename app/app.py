import requests
import os
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MYSQL_URI']
# Нужно потому что создали базу в MySQL вручную!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class NewCity(db.Model):

    __tablename__ = 'new_city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Создаем таблицы в БД
db.create_all()

@app.route('/')
def index():
    cities = NewCity.query.all()

    url = 'http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=4340da7e563b11187cf58bb997d62303'
    weather_data = []


    for city in cities:

        r = requests.get(url.format(city.name)).json()
	
        weather = {
            'city': city.name,
            'temperature': r['list'][0]['main']['temp'],
            'description': r['list'][0]['weather'][0]['description'],
            'icon': r['list'][0]['weather'][0]['icon'],
        }
        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)


@app.route('/add-city/', methods=['POST'])
def add_city():
    name = request.form.get('city', '')

    if not name:
        return redirect('/')

    c = NewCity(name=name)
    db.session.add(c)
    db.session.commit()

    return redirect('/')
