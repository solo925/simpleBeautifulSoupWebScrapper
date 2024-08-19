from bs4 import BeautifulSoup
import requests

url = "https://cryptomarketcap.com/"

result = requests.get(url).text

doc = BeautifulSoup(result,"html.parser")
tbody = doc.tbody

# print(len(td_elements))

trs=tbody.contents
# print(list(trs[0].next_siblings))
# print(list(trs[1].previous_siblings))
# print(trs[0].parents)
# print(trs[0].parent.name)
# print(list(trs[0].descendants))

prices = {}
for tr in trs:
    
    
    name= tr.contents[2]
    fixed_name = name.p.string
    price=tr.contents[6]
    fixed_price = price.string
    
    prices[fixed_name]=fixed_price
    
    
print(prices)
  
    
   
        
       
        
   


