#----------------------------------------------------------------------------------------
# below code is used to read data from given url and counting the words used in the data using nltk.
#https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-a2601e8619e5
#----------------------------------------------------------------------------------------
# importing required modules
import requests
from bs4 import BeautifulSoup
import nltk
import pandas as pd 
import re 
#url = 'https://timesofindia.indiatimes.com/business/india-business/nclat-restores-cyrus-mistry-as-executive-chairman-of-tata-group/articleshow/72868385.cms'
url = 'http://books.toscrape.com/'
'''
a = url.split('/')
print(a) #output is ['http:', '', 'books.toscrape.com', '']
a= "/".join(url.split("/"))
print(a) # output is http://books.toscrape.com/
a = "/".join(url.split("/")[:-1])
print(a) #output = http://books.toscrape.com
a = "/".join(url.split("/")[:-1]) + "/"
print(a) # output is http://books.toscrape.com/

page = requests.get(url)
#a = page.text[:2000]
#print(a)
# result of 'a' is quite messy! Let’s make this more readable using BeautifulSoup
soup = BeautifulSoup(page.text,'html.parser')
#print(soup.prettify()[:2000])
#first step consist in finding the URL of every book product page. for this artical-div-a(where url of book product page).
#a = soup.find("article", class_ = "product_pod").div.a.get('href')
#print(a)
# to get all urls of the page
main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]
print(str(len(main_page_products_urls)) + " fetched products URLs")
print("One example: %s" %main_page_products_urls[0])
a = "/".join(url.split("/")[:-1]) + "/" +main_page_products_urls[0]
print(a) # output is http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
# same information can be retrived with below multiple lines of code 
#count = 0
#for x in soup.findAll("article", class_ = "product_pod"):
#    main_page_products_urls = x.div.a.get('href')
#    #print(main_page_products_urls)
#    count = count +1    
#print('total product urls are:- %s' %count)
#print("One example: %s" %main_page_products_urls)
main_url = url
# find same URL pattern ‘catalogue/category/books’. using BeautifulSoup
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
categories_urls = [main_url + x.get('href') for x in soup.find_all("a", href=re.compile("catalogue/category/books"))]
#print(categories_urls) # output is ['http://books.toscrape.com/catalogue/category/books_1/index.html', 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html', 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html', 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html', 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html', 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html', 'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html', 'http://books.toscrape.com/catalogue/category/books/romance_8/index.html', 'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html', 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html', 'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html', 'http://books.toscrape.com/catalogue/category/books/religion_12/index.html', 'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html', 'http://books.toscrape.com/catalogue/category/books/music_14/index.html', 'http://books.toscrape.com/catalogue/category/books/default_15/index.html', 'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html', 'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html', 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html', 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html', 'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html', 'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html', 'http://books.toscrape.com/catalogue/category/books/science_22/index.html', 'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html', 'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html', 'http://books.toscrape.com/catalogue/category/books/art_25/index.html', 'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html', 'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html', 'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html', 'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html', 'http://books.toscrape.com/catalogue/category/books/humor_30/index.html', 'http://books.toscrape.com/catalogue/category/books/horror_31/index.html', 'http://books.toscrape.com/catalogue/category/books/history_32/index.html', 'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html', 'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html', 'http://books.toscrape.com/catalogue/category/books/business_35/index.html', 'http://books.toscrape.com/catalogue/category/books/biography_36/index.html', 'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html', 'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html', 'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html', 'http://books.toscrape.com/catalogue/category/books/academic_40/index.html', 'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html', 'http://books.toscrape.com/catalogue/category/books/historical_42/index.html', 'http://books.toscrape.com/catalogue/category/books/christian_43/index.html', 'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html', 'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html', 'http://books.toscrape.com/catalogue/category/books/novels_46/index.html', 'http://books.toscrape.com/catalogue/category/books/health_47/index.html', 'http://books.toscrape.com/catalogue/category/books/politics_48/index.html', 'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html', 'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html', 'http://books.toscrape.com/catalogue/category/books/crime_51/index.html']
categories_urls = categories_urls[1:] '''
'''print(categories_urls) #output will display wothout 'http://books.toscrape.com/catalogue/category/books_1/index.html' because it corresponds to all the books
print(str(len(categories_urls)) + " fetched categories URLs")
print("Some examples: %s" %(categories_urls[:5])) # will display 5 urls.
'''
def getAndParseURL(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return(soup)

def getBooksURLs(url):
    soup = getAndParseURL(url)
    # remove the index.html part of the base url before returning the results
    return(["/".join(url.split("/")[:-1]) + "/" + x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")])

# Now Scrape to gather data about all books data of the website. below code explains to get data from multiple pages.
'''# store all the results into a list
pages_urls = [main_url]
#page = requests.get(pages_urls[0])
#soup = BeautifulSoup(page.text,'html.parser')
soup = getAndParseURL(pages_urls[0])
# while we get two matches, this means that the webpage contains a 'previous' and a 'next' button
# if there is only one button, this means that we are either on the first page or on the last page
# we stop when we get to the last page
while len(soup.findAll("a", href=re.compile("page"))) == 2 or len(pages_urls) == 1:
    # get the new complete url by adding the fetched URL to the base URL (and removing the .html part of the base URL)
    new_url = "/".join(pages_urls[-1].split("/")[:-1]) + "/" + soup.findAll("a", href=re.compile("page"))[-1].get("href")
    #print(new_url)
    # add the URL to the list
    pages_urls.append(new_url)
    # parse the next page
    soup = getAndParseURL(new_url)
print(str(len(pages_urls)) + " fetched URLs")
print("Some examples:- %s" % pages_urls[:5]) # output is ['http://books.toscrape.com/', 'http://books.toscrape.com/catalogue/page-2.html', 'http://books.toscrape.com/catalogue/page-3.html', 'http://books.toscrape.com/catalogue/page-4.html', 'http://books.toscrape.com/catalogue/page-5.html']
'''
# below code will explain if page found(=200) and page not found(=404)
pages_urls = []
new_page = "http://books.toscrape.com/catalogue/page-1.html"
while requests.get(new_page).status_code == 200:
    pages_urls.append(new_page)
    new_page = pages_urls[-1].split("-")[0] + "-" + str(int(pages_urls[-1].split("-")[1].split(".")[0]) + 1) + ".html"
#print(str(len(pages_urls)) + " fetched URLs")
#print("Some examples:- %s" % pages_urls[:5])

#Now the next step consists in fetching all the products URLs for every page.
#This step is quite simple as we already have the list of all pages and the function to get products URLs from a page.
booksURLs = []
for page in pages_urls:
    booksURLs.extend(getBooksURLs(page))
#print(str(len(booksURLs)) + " fetched URLs")
#print("Some examples: %s" %(booksURLs[:2]))
#The last step consist in scraping the data for each product. Let’s explore first how the information is structured on the products pages:
#We can easily retrieve a lot of information for every book: book title, price, availability, image, category, rating
# let's do it
names = []
#prices = []
#nb_in_stock = []
#img_urls = []
#categories = []
#ratings = []
# scrape data for every book URL: this may take some time
for url in booksURLs:
    soup = getAndParseURL(url)
    # product name
    names.append(soup.find("div", class_ = re.compile("product_main")).h1.text)
    # product price
#    prices.append(soup.find("p", class_ = "price_color").text[2:]) # get rid of the pound sign
    # number of available products
#    nb_in_stock.append(re.sub("[^0-9]", "", soup.find("p", class_ = "instock availability").text)) # get rid of non numerical characters
    # image url
#    img_urls.append(url.replace("index.html", "") + soup.find("img").get("src"))
    # product category
#    categories.append(soup.find("a", href = re.compile("../category/books/")).get("href").split("/")[3])
    # ratings
#    ratings.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])
# add data into pandas df
scraped_data = pd.DataFrame({'name': names})
#scraped_data = pd.DataFrame({'name': names, 'price': prices, 'nb_in_stock': nb_in_stock, "url_img": img_urls, "product_category": categories, "rating": ratings})
print(scraped_data.head())