import datetime
import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/date')
def date_html():
	return render_template('date.html', mydate = datetime.datetime.now().strftime('%d.%m.%Y'))


@app.route('/time')
def time_html():
	return render_template('time.html', mytime = datetime.datetime.now().strftime('%H:%M:%S'))

@app.route('/weather')
def weather_html():
	result = requests.get('http://api.openweathermap.org/data/2.5/weather/?units=metric&q=Moscow&appid=8386d899dce8b64e7b96fde19678d5f6')
	if result.status_code == 200:
		return render_template('weather.html', myweather=result.json())
	else:
		return render_template('error.html', status=result.status_code)

if __name__ == "__main__":
	app.run(debug=True)