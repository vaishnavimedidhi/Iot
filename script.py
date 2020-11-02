from flask import *   
import sys
from Adafruit_IO import Client,Feed,RequestError , MQTTClient
import requests
import json
from flask_mail import *  

app = Flask(__name__)
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'srivaishnavi1956@gmail.com'  
app.config['MAIL_PASSWORD'] = 'medidhivenkatganesh'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True     
mail = Mail(app) 

ADAFRUIT_IO_KEY = 'ec532d808bfd4f6a949c601fe932e5d5'
ADAFRUIT_IO_USERNAME = 'vaish1599'
FEED_ID = 'welcome-feed'
def index():  
    msg = Message(subject = "Meat Freshness", body = "your meat is decaying!!!", sender = "srivaishnavi1956@gmail.com", recipients = ["kuttralamvc@gmail.com"])  
    with app.open_resource("alert.png") as fp:  
        msg.attach("alert.png","image/png",fp.read())  
        mail.send(msg)  
    print("sent mail")
    return "sent"


@app.route('/')   
def home():
    URL = 'https://io.adafruit.com/api/v2/kuttralam/feeds/pot-data/data?X-AIO-Key=ec532d808bfd4f6a949c601fe932e5d5'
    r = requests.get(URL)
    data = r.json()
    data = json.loads(r.content)
    URL_last ='https://io.adafruit.com/api/v2/kuttralam/feeds/pot-data/data/last?X-AIO-Key=ec532d808bfd4f6a949c601fe932e5d5'
    r = requests.get(URL_last)
    data_last = r.json()
    data_last = json.loads(r.content)
    if(int(data_last['value'])>550):
        index()
    return render_template('home.html' , data = data)




if __name__ =='__main__':  
    app.run(debug = True)  