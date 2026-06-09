import requests

API_KEY="fa0693990efe0eb39597a7155ee84143"

url=f"https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={API_KEY}&units=metric"

response=requests.get(url)

print(response.json())