import requests
from bs4 import BeautifulSoup
import json

# CAD Dollar
def printCADtoUSD():
	html = requests.get("https://www.bankofcanada.ca/")
	soup = BeautifulSoup(html.content, "html.parser")
	cad = soup.get_text()
	cad = cad[cad.index("titlesHomepageChart"):cad.index("subTitlesHomepageChart")]
	cad_json = cad.replace("titlesHomepageChart = ", "").replace(";", "")
	cad_json = json.loads(cad_json)
	print(cad_json['USD'])

printCADtoUSD()



