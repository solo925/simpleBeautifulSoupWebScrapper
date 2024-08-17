from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/Processors-Desktops/SubCategory/ID-343/Page-1"

result= requests.get(url).text
# result.text
doc = BeautifulSoup(result,"html.parser")
prices = doc.find_all(string="$")

parent = prices[0].parent

strong = parent.strong.string

print(strong)

# print(doc.prettify())
