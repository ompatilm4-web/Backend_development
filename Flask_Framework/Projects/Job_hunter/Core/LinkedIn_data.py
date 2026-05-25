import bs4 
import requests
import time 


Data =requests.get("https://www.linkedin.com/company/microsoft/").text
soup=bs4.BeautifulSoup(Data,'html.parser')
print(soup.prettify())
