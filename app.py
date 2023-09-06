from flask import Flask,render_template,request

import requests

app = Flask(__name__)

api_key = 'c00b43b2d8e3bc0c97552995864c9d3d'


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/weather', methods = ["GET","POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        data=weather_data.json()
        return render_template ("index.html",temp=data.get("main").get("temp"),feels=data.get("main").get("feels_like"),pressure=data.get("main").get("pressure"),humidity=data.get('main').get("humidity"),wind=data.get("wind").get("speed"),name=data.get("name"),sunrise=data.get("sys").get("sunrise"),sunset=data.get("sys").get("sunset"),clouds=data.get("weather")[0].get("description"))
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(debug=True)