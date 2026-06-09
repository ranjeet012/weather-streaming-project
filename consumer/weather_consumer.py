from kafka import KafkaConsumer

from sqlalchemy import create_engine

import pandas as pd

from urllib.parse import quote_plus

import json

password = quote_plus("Ranjeet@143")   # apna actual password

engine=create_engine(

f"mysql+pymysql://root:{password}@localhost/weather_project"

)

consumer=KafkaConsumer(

"weather_topic",

bootstrap_servers='localhost:9092',

value_deserializer=lambda x: json.loads(x.decode('utf-8'))

)

for msg in consumer:

    data=msg.value

    df=pd.DataFrame([{

        "city":data["city"],

        "temperature":data["temperature"],

        "humidity":data["humidity"],

        "weather_condition":data["condition"]

    }])

    df.to_sql(

        "weather_data",

        engine,

        if_exists="append",

        index=False

    )

    print("Inserted:",data)