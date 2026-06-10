import requests

API_KEY="Enter weather api key here"

url=f"https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={API_KEY}&units=metric"

response=requests.get(url)

print(response.json())
