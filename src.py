# coding=utf-8

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


def get_html_page(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(link)
    html = driver.page_source.encode('utf-8')
    return (html)


def parse_page(html_page):
    target = '<span id="price_inside_buybox" class="a-size-medium a-color-price">'
    html_page.find(target)
    splice1 = html_page[html_page.find(target)+len(target):]
    splice2 = splice1[:splice1.find('&')]
    price = int(splice2[:splice2.find(',')].split()[0])
    return price


expected = 100000

link1 = 'https://www.amazon.it/gp/product/B08FRJ78PR/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1'
link2 = 'https://www.amazon.it/gp/product/B08FRJ78PR/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1'
link3 = 'https://www.amazon.it/gp/product/B08FRJ78PR/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1'

print(parse_page(get_html_page(link1)))

list_link = [
    link1, link2, link3
]

for link in list_link:
    price = parse_page(get_html_page(link))
    if price <= expected:
        print('Price: '+str(price) + ' buy it')
    else:
        print('Price: '+str(price) + ' DO NOT buy it')
