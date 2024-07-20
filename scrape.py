import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import json

print("~ Initiating Web Scraping...")
data=[]

base_url = "https://www.amazon.com"
url = "https://www.amazon.in/gp/bestsellers/books/1318132031/ref=zg_bs_nav_books_2_1318128031"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

count = 0
top = 10

product = soup.find_all("div", class_ = "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y")
titles = []
authors = []
bdgs = []
for i in range(0,100,2):
    titles.append(product[i].text)
    authors.append(product[i+1].text)
bdg_cont = soup.find_all("span", class_ = "zg-bdg-text")
for i in bdg_cont:
    bdgs.append(i.text)

for i in range(len(titles)):
    book = {"BestSeller":bdgs[i],"Title":titles[i], "Author":authors[i]}
    data.append(book)

df = pd.DataFrame(data)
print(df)
df.to_csv('books.csv', header=False, index=False)
file = open('books.json', mode='w', encoding='utf-8')
file.write(json.dumps(data))