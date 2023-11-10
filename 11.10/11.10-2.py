#HTML

""" from bs4 import BeautifulSoup as bs
import requests as rq

#url = "https://xkcd.com/2852/"
url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

pres = res_html.find("h1")
print(pres)
print("\n1-----------\n")
print(pres.get_text().strip())
print("\n2---------------\n")
print(pres.next_element.get_text().strip())
print("\n6-----------------------\n")
print(pres.get_text())
 """
""" from bs4 import BeautifulSoup as bs
import requests as rq

#url = "https://xkcd.com/2852/"
url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

pres = res_html.find("h2")
print(pres)
print("\n1-----------\n")
print(pres.get_text().strip())
print("\n2---------------\n")
print(pres.next_element.get_text().strip())
print("\n6-----------------------\n")
print(pres.get_text())

tres = res_html.find("title")
print(pres)
print("\n3-----------\n")
print(tres.text_element)
print("\n4---------------\n")
print(tres.get_text().strip())



fares = res_html.findAll("a")
print(fares)
print("\ns--------------------------------------\n")

clres = res_html.findAll(class_="doc-title")
print(clres)

print("\n6---------------------------------\n")
clrs = res_html.find(class_="head_top")
print(clrs)
print(clrs.get_text()) """

#select_one
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

# print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
#print(ut)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
#print(goods)
print(goods.get_text()) """


#select

from bs4 import BeautifulSoup as bs
import requests as rq

url = "thhps://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
#print(iss)
print("\n--------------------------------------------\n")

for i in iss :
    issue = i.get_text()
    print(issue)
    
print("\n---------------------------------------\n")
ct=res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attr["data-tiara-custom"]
    print(c +"\n")