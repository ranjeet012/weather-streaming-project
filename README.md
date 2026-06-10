# Real-Time Weather Data Streaming Pipeline

## Project Overview

This project demonstrates an end-to-end real-time data engineering pipeline that collects weather data from the OpenWeather API, streams it through Apache Kafka, stores it in MySQL, and visualizes insights using Power BI.

The objective of this project is to simulate a real-world streaming data pipeline and understand how data moves through different layers of a modern data engineering architecture.
---

## Architecture

OpenWeather API
↓
Python Producer
↓
Apache Kafka
↓
Kafka Topic (weather_topic)
↓
Python Consumer
↓
MySQL Database
↓
Power BI Dashboard

---

## Tech Stack

| Technology      | Purpose                     |
| --------------- | --------------------------- |
| Python          | Data Ingestion & Processing |
| Apache Kafka    | Real-Time Streaming         |
| OpenWeather API | Data Source                 |
| MySQL           | Data Storage                |
| SQLAlchemy      | Database Connection         |
| Pandas          | Data Transformation         |
| Power BI        | Data Visualization          |
| Git & GitHub    | Version Control             |

---

## Project Structure

weather_streaming_project/

├── producer/

│ └── weather_producer.py

│

├── consumer/

│ └── weather_consumer.py

│

├── dashboard/

│ ├── Weather_Dashboard.pbix

│

└── README.md

---

## Folder Description

### producer/

Responsible for extracting weather data from the OpenWeather API and publishing messages to Kafka.

File:

weather_producer.py

Functions:

* Connect to OpenWeather API
* Fetch weather data
* Convert response to JSON
* Send messages to Kafka topic

---

### consumer/

Responsible for consuming weather data from Kafka and storing it in MySQL.

File:

weather_consumer.py

Functions:

* Read messages from Kafka topic
* Deserialize JSON messages
* Convert to DataFrame
* Insert records into MySQL

---

### database/

Contains SQL scripts used to create databases and tables.

Example:

weather_project

weather_data

---

### dashboard/

Contains Power BI dashboard files.

Files:

Weather_Dashboard.pbix

Dashboard Screenshots

---

## Database Design

Database:

weather_project

Table:

weather_data

Columns:

| Column Name       | Description            |
| ----------------- | ---------------------- |
| id                | Unique Identifier      |
| city              | City Name              |
| temperature       | Temperature in Celsius |
| humidity          | Humidity Percentage    |
| weather_condition | Weather Description    |
| created_at        | Record Timestamp       |

---

## Kafka Components

### Kafka Topic

weather_topic

### Producer

Publishes weather data every 30 seconds.

### Consumer

Reads data from Kafka and inserts records into MySQL.

---

## Data Flow

Step 1

Producer fetches weather data from OpenWeather API.

Step 2

Producer sends data to Kafka topic.

Step 3

Kafka stores messages temporarily.

Step 4

Consumer reads messages from Kafka.

Step 5

Consumer inserts data into MySQL.

Step 6

Power BI reads data from MySQL.

Step 7

Dashboard displays weather insights.

---

## Sample Weather Record

{
"city": "Mumbai",
"temperature": 31.5,
"humidity": 78,
"condition": "Clouds"
}

---

## Power BI Dashboard

The dashboard contains:

### KPI Cards

* Average Temperature
* Average Humidity

### Charts

* Temperature Trend Over Time
* Weather Condition Distribution

## Key Insights

The dashboard helps answer:

* What is the average temperature?
* What is the average humidity?
* How is temperature changing over time?
* Which weather condition occurs most frequently?

---

## Installation Steps

### Clone Repository

git clone <repository_url>

### Create Virtual Environment

python -m venv venv

### Activate Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Required Python Libraries

kafka-python

requests

pandas

sqlalchemy

pymysql

---

## Run Kafka

Start Kafka Broker

bin\windows\kafka-server-start.bat config\server.properties

Create Topic

bin\windows\kafka-topics.bat --create --topic weather_topic --bootstrap-server localhost:9092

---

## Run Consumer

python consumer/weather_consumer.py

---

## Run Producer

python producer/weather_producer.py

---

## Future Improvements

* Multiple City Support
* Docker Containerization
* Airflow Scheduling
* AWS Deployment
* Real-Time Streaming Dashboard
* Spark Streaming Integration

---

## Skills Demonstrated

* Python Programming
* API Integration
* Kafka Streaming
* Real-Time Data Processing
* MySQL
* ETL Pipelines
* Data Visualization
* Power BI
* Git & GitHub

## Author

Ranjeet Pal

Data Engineering Portfolio Project
