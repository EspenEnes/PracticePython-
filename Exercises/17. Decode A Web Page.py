from bs4 import BeautifulSoup
import requests

url = 'http://www.vg.no'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

articles = soup.find_all("div", class_="article-extract")

article = [articles.div in articles]











