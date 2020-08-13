#######-----------------WEB SCRAPING--------------##############

from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages = []
prices = []
stars = []
titles = []
urlss = []

## to get page links(page1, page2....)
pages_to_scrape = 2
for i in range(1, pages_to_scrape+1):
    url = ("http://books.toscrape.com/catalogue/page-{}.html").format(i)
    pages.append(url)
#print(pages)


## getting the all items(webELements) in the pages(1,2,...)
for item in pages:
    page = requests.get(item) ## checking the response <200>
    #print(page)
    soup = bs4(page.text, 'html.parser') # change text to webElement
    #print (soup.prettify())


    # getting Title of the book
    for i in soup.find_all('h3'): 
        tt1 = i.getText()
        #print(tt1)
        titles.append(tt1)
    #print(titles)


    ## getting the price of the book   
    for j in soup.find_all('p', class_='price_color'):
        price = j.getText()
        #print(price)
        prices.append(price)


    ## getting the star rating  of the book
    for s in soup.find_all('p', class_='star-rating'):
        for k,v in s.attrs.items():
            #print(k,v)
            ## getting 2nd values(star number) of the kv pairs
            star = v[1]
            #print(star)
            stars.append(star)

    ## getting image of the books
    divs = soup.find_all('div', class_='image_container')
    for thumbs in divs:
        tgs = thumbs.find('img', class_='thumbnail')
        # adding https website link to the tgs to get whole image link
        urls = 'http://books.toscrape.com/'+ str(tgs['src'])
        # link will have /.../ which we have to remove and replace with null
        newurls = urls.replace(".../ ", "")
        #print(newurls)
        urlss.append(newurls)
        #print(urlss)


# Saving scraped data in dict format
data = {'Titles': titles, 'Prices': prices, 'Stars': stars, 'URL':urlss}
#print(data)

df = pd.DataFrame(data=data)

df.index+=1

## Saving as a CSV file
df.to_csv( 'D:\\WebScrap\\Book_scrape\\output.csv')



