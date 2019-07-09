from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
headings = soup.findAll("h2", {"class": "css-78b01r"})
print(headings)

for heading in headings:
    if heading.findAll("span"):
        # .strip() removes leading/trailing whitespace
        print(heading.a.text.strip())
    else:
        print(heading.text)
