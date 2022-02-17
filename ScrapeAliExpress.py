#!/usr/bin/env python
# coding: utf-8

# https://www.jcchouinard.com/web-scraping-with-python-and-requests-html/
# https://pypi.org/project/requests-html/


import pyppdf.patch_pyppeteer
import requests
from bs4 import BeautifulSoup as soup
from requests_html import AsyncHTMLSession, HTMLSession
import asyncio




header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

html = requests.get('https://www.aliexpress.com/item/32867673917.html?spm=a2g0o.productlist.0.0.3154230d1ytBWE&algo_pvid=6ae5a1f8-b315-44cf-998d-2e38664bd259&algo_expid=6ae5a1f8-b315-44cf-998d-2e38664bd259-0&btsid=0ab6fb8315916032919967411e2635&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_',headers=header,)

cookies = html.cookies

html = requests.get('https://www.aliexpress.com/item/32867673917.html?spm=a2g0o.productlist.0.0.3154230d1ytBWE&algo_pvid=6ae5a1f8-b315-44cf-998d-2e38664bd259&algo_expid=6ae5a1f8-b315-44cf-998d-2e38664bd259-0&btsid=0ab6fb8315916032919967411e2635&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_',headers=header,cookies=cookies)

# html.status_code

bsobj = soup(html.content, 'html.parser')


bsobj.findAll('span',{'calss':'product-price-value'})

async def getLink():
    asession = AsyncHTMLSession()
    r = await asession.get('https://www.aliexpress.com/item/32867673917.html?spm=a2g0o.productlist.0.0.3154230d1ytBWE&algo_pvid=6ae5a1f8-b315-44cf-998d-2e38664bd259&algo_expid=6ae5a1f8-b315-44cf-998d-2e38664bd259-0&btsid=0ab6fb8315916032919967411e2635&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_')

    await r.html.arender()

    h1 = r.html.find('h1')
    print(f'{h1[0].text = }')

    rating = r.html.find('.overview-rating-average')
    print(f'{rating[0].text = }')

    rating_count = r.html.find('.product-reviewer-reviews')
    print(f"{rating_count[0].text.replace('Reviews','').strip() = }")

    price = r.html.find('.product-price-value')
    price[0].text.replace('US','').strip()

    print(f'{r.html.absolute_links = }')

async def async_main():
    await getLink()

async def main():
    await asyncio.create_task(async_main())

asyncio.set_event_loop(asyncio.ProactorEventLoop())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# loop.close()
