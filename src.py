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

link1 = 'https://www.amazon.it/Notebook-Dell-Touch-Intel-i5-7200U/dp/B07D4BKZ8T/ref=sr_1_2?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=dell+xps&qid=1617314228&sr=8-2'


link2='https://www.amazon.it/Dell-S2721QS-Schermo-60Hz-FreeSync/dp/B08FRJ9RJ9/ref=sr_1_1?adgrpid=115458825962&dchild=1&gclid=CjwKCAjw3pWDBhB3EiwAV1c5rGM3Pt7nEzc_EUkAxVQvz5kB4eQP3Mg0L32nG6f21RwPukOVau29MBoCOiYQAvD_BwE&hvadid=482602933651&hvdev=c&hvlocphy=1008038&hvnetw=g&hvqmt=e&hvrand=8870699896758541578&hvtargid=kwd-948125000784&hydadcr=16639_1782715&keywords=s2721qs&qid=1617316177&sr=8-1'

link3='https://www.amazon.de/dp/B014VDSKDA?ref_=Oct_DLandingS_D_ad603cd6_NA'

list_link = [
    link1,link2,link3
]

for link in list_link:
    price = parse_page(get_html_page(link))
    if price<=expected:
        print('Price: '+str(price) + ' buy it')
    else:
        print('Price: '+str(price) + ' DO NOT buy it')