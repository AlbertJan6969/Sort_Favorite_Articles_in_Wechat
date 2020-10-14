'''
from selenium import webdriver

chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
url = 'https://mp.weixin.qq.com/s/QNTXg9XaIrEF6pj9LAaEmg'
browser.get(url)
NAME=browser.find_element_by_id("activity-name")
AUTHOR=browser.find_element_by_id("js_name")
WEB=url
print(NAME)
print(AUTHOR)
print(WEB)
'''

x=1
print("Do you need to print the author of articles")
print("A: need, B: no need")
Decide_author=input()
from requests_html import HTMLSession
session=HTMLSession()
url_list=[]
print("Now you need to add some url, when you are finish, type STOP")

while x>0:
    print("New URL")
    entered_url=input()
    if entered_url=="STOP":
        break
    url_list.append(entered_url)

NUMBER=len(url_list)
for x in range (1,NUMBER+1):
    url = url_list.pop()
    r = session.get(url)
    print(url)
    sel = '#activity-name'
    results = r.html.find(sel)
    print(results[0].text)
    sel = '#js_name'
    results = r.html.find(sel)
    if Decide_author=="A":
        print(results[0].text)

print("enter anything to quit")
input()




