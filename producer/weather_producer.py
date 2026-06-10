from kafka import KafkaProducer

import requests

import json

import time

producer=KafkaProducer(

bootstrap_servers='localhost:9092',

value_serializer=lambda x: json.dumps(x).encode('utf-8')

)

API_KEY="Enter your Weather api key here"

while True:

    url=f"https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={API_KEY}&units=metric"

    data=requests.get(url).json()

    weather={

        "city":data["name"],

        "temperature":data["main"]["temp"],

        "humidity":data["main"]["humidity"],

        "condition":data["weather"][0]["main"]

    }

    producer.send(

        "weather_topic",

        weather

    )

    print(weather)

    time.sleep(30)
