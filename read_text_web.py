# belwo code is to read the data from url
#from urllib.request import Request, urlopen   # to open url
import requests
from bs4 import BeautifulSoup   # to read the context of html page
import nltk
url='https://timesofindia.indiatimes.com/business/india-business/nclat-restores-cyrus-mistry-as-executive-chairman-of-tata-group/articleshow/72868385.cms'
page = requests.get(url).text
soup = BeautifulSoup(page,'html.parser')
#soup = soup.find(class_="col-md-10 col10-s fl")
soup = soup.find('div',{"class":"embedarticle"})
for p in soup.find_all():
    text = p.get_text()
tokens = nltk.word_tokenize(text)
text =nltk.Text(tokens)
#num_words = nltk.corpus.gutenberg.words(text)
count=0
for words in text:
    a = len(words)
    #print('length of "%s" is:- %s'%(words,a))
    count = count+1
print('total number of words are:- %s'%(count))   
dist_words = len(set(w.lower() for w in text))
print('total number of distinct words are:- %s'%(dist_words))
words =  set(w.lower() for w in text)
for w in sorted(words): # using sorted function to sort the words 
    print(w)
    
    
'''    
#print('total number of words used are :- %s' %(count))
#response = request.urlopen(url)
#response = urlopen(url).read().decode('utf8')
# we need a parser,Python built-in HTML parser is enough . 
#raw=BeautifulSoup(response,'html.parser').get_text() 
#tokens =nltk.word_tokenize(raw)
#print(tokens)
#text = nltk.Text(tokens)
#for t in text:
#    print(t)
#a = len(raw)
#print(a)
#b = raw[:73]
#print(b)
'''