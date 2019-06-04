from bs4 import BeautifulSoup
import requests

#page = requests.get('https://www.nyandcompany.com/search/?Dy=1&Nty=1&Ntp=1&Ntt=quijibo')
page = requests.get('https://www.nyandcompany.com/search/?Dy=1&Nty=1&Ntp=1&Ntt=socks')
soup = BeautifulSoup(page.content, 'html.parser')
#soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())
#print(soup.get_text())
#print(soup.find(text="We found "))

