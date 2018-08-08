import requests
from bs4 import BeautifulSoup


# Weather
def get_weather():
    # Enter your city's url from weather.com
    html = requests.get("https://weather.com/en-CA/weather/today/l/cd81ca7148657b33cf62a3e49a47ed674be8b06e8a66ea1d91c9326b9ac0d784")
    soup = BeautifulSoup(html.content, "html.parser")

    weatherTEMP = soup.find("div", class_="today_nowcard-temp").span.get_text()
    weatherFEELS = soup.find("span", classname="deg-feels").get_text()

    print("Current temp: " + weatherTEMP + "\t Feels like: " + weatherFEELS)

get_weather()
