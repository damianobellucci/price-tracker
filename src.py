#download the chromedriver from https://chromedriver.chromium.org
#coding=utf-8

from selenium import webdriver
import time

def get_html_page(link):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(link)

    html = driver.page_source.encode('utf-8')

    return (html)

def parse_page(html_page):
    target = '<span id="price_inside_buybox" class="a-size-medium a-color-price">'
    splice1 = html_page[ html_page.find(target)+len(target):]
    splice2 = splice1[:splice1.find('&')]
    price = int(splice2[:splice2.find(',')].split()[0])
    return price

#print(get_html_page())     

#file1=open("text.html","w")
#file1.write(get_html_page())
#file1.close()


expected=100000

link1 = ''


link2=''

link3=''

list_link = [
    link1,link2,link3
]

for link in list_link:
    price = parse_page(get_html_page(link))
    if price<=expected:
        print('Price: '+str(price) + ' buy it')
    else:
        print('Price: '+str(price) + ' DO NOT buy it')