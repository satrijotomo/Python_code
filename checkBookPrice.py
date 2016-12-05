#! /usr/bin/env python3
### this file was created on Mac system

import bs4,requests

def getBNBookPrice(ProductUrl):
    res = requests.get(ProductUrl)
    mySoup = bs4.BeautifulSoup(res.text, "html.parser")
    title = mySoup.select('#prodSummary > h1')
    elems = mySoup.select('#prodInfoContainer > form.pdp-form > p > span.price.current-price')
    print('The price of "'+title[0].text+'" book is :' +elems[0].text)


print("Enter the Barnes and Nobles book URL: ")
theUrl = input()
print("Getting the book price for "+theUrl+". Please wait ...\n")
getBNBookPrice(theUrl)
