# https://www.youtube.com/watch?v=xvqsFTUsOmc&t=1952s
# Web scraping, pickle imports
import requests
from bs4 import BeautifulSoup
import pickle

# We can either keep it in dictionary format or put it into a pandas dataframe
import pandas as pd

# Apply a first round of text cleaning techniques
import re
import string

# We are going to create a document-term matrix using CountVectorizer, and exclude common English stop words.
# with CountVectorizer, we can remove stop words. Stop words are common words that add no additional meaning to text such as 'a', 'the', etc.
from sklearn.feature_extraction.text import CountVectorizer

# Look at the most common top words --> add them to the stop word list
from collections import Counter

# Let's update our document-term matrix with the new list of stop words
from sklearn.feature_extraction import text 
from sklearn.feature_extraction.text import CountVectorizer

# Let's make some word clouds!
# Terminal / Anaconda Prompt: conda install -c conda-forge wordcloud
from wordcloud import WordCloud
# Reset the output dimensions
import matplotlib.pyplot as plt

# Scrapes transcript data from scrapsfromtheloft.com
# Getting the data from url and loading to a file 
def url_to_transcript(url):
    '''Returns transcript data specifically from scrapsfromtheloft.com.'''
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="post-content").find_all('p')]
    print(url)    
    #print(text)
    '''# getting one paragraph
    count=0
    for text in text:
        print(count)
        print(text)
        count = count+1
        if count <2:
            break'''
    return text

urls = 'http://scrapsfromtheloft.com/2017/09/19/ali-wong-baby-cobra-2016-full-transcript/'
transcript  = url_to_transcript(urls)
#print(transcript)
# Comedian names
comedians = ['ali']
# Creating files in the path based on commedian names with the context/data
for i, c in enumerate(comedians):
    with open(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\transcripts/' + c + ".txt", "wb") as file:   
        pickle.dump(transcript, file) # entire data will load into the file.
        #pickle.dump(transcript[i], file) # need to test this.
        
# Load / Display pickled files
data = {}
for i, c in enumerate(comedians):
    with open(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\transcripts/' + c + ".txt", "rb") as file:   
    #with open('transcripts/' + c + ".txt", "rb") as file:
        data[c] = pickle.load(file)
#print(data.keys()) # performing checks
#print(data['ali']) # performing checks
a = data.items()
#print('items are:- %s'%(a))
#cleaning the data
a = next(iter(data.keys()))
#print(a)
b = next(iter(data.values())) # data will be in list ex:- ['Ladies and gentlemen, please welcome to the stage: Ali Wong! Hi. Hello! Welcome! Thank you! Thank you for coming.]
#print(b)
# now we will convert list to string formate
# We are going to change this to key: comedian, value: string format
def combine_text(list_of_text):
    '''Takes a list of text and combines them into one large chunk of text.'''
    combined_text = ' '.join(list_of_text)
    #print(combine_text)
    return combined_text
#combine_text(data.values())
# Combine it!
data_combined = {key: [combine_text(value)] for (key, value) in data.items()}

# We can either keep it in dictionary format or put it into a pandas dataframe
pd.set_option('max_colwidth',150)
data_df = pd.DataFrame.from_dict(data_combined).transpose()
data_df.columns = ['transcript']
#print(data_df.columns)
data_df = data_df.sort_index()
data_df
#print(data_df)

# Let's take a look at the transcript for Ali Wong
a = data_df.transcript.loc['ali']
#print(a)
# Apply a first round of text cleaning techniques
def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    #print('text after changing to lower case:- %s' %(text))
    text = re.sub('\[.*?\]', '', text) # removes brackets.
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # removes punctuation markes from a string.
    text = re.sub('\w*\d\w*', '', text) # \w* means remove numbers from a string \d removes digitis from string.
    return text
round1 = lambda x: clean_text_round1(x) # lambda is an anonymous function in python which used at run time.
#print(round1)
# Let's take a look at the updated text
#----------------------------------------------------------------
# other way to use apply function in pandas
#df = pd.read_csv(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\transcripts\ali.txt', encoding="ISO-8859-1", error_bad_lines=False)
#print(df)
#dfobj = pd.DataFrame(df, columns = list('a'))
#print(dfobj)
#modobj = [clean_text_round1(x) for x in dfobj]
#modobj = dfobj['a'].apply(clean_text_round1)
#print('clean data:- '+ str(modobj))
#----------------------------------------------------------------
data_clean = pd.DataFrame(data_df.transcript.apply(round1)) # apply is padans function to pass arguments to a function. In this example we are passing data_df.transcript data to clean_text_round1 function to remove unwanted characters'. Here transcript is a column name and data_df is pandas dataframe.
data_clean


# Apply a second round of cleaning
def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

round2 = lambda x: clean_text_round2(x)
# Let's take a look at the updated text
data_clean = pd.DataFrame(data_clean.transcript.apply(round2))
#data_clean

# Let's take a look at our dataframe
data_df
#print(data_df)
# Let's add the comedians' full names as well
full_names = ['Ali Wong']

data_df['full_name'] = full_names
data_df
#print(data_df)

# Let's pickle it for later use
data_df.to_pickle(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\corpus.pkl')

# We are going to create a document-term matrix using CountVectorizer, and exclude common English stop words
#with CountVectorizer, we can remove stop words. Stop words are common words that add no additional meaning to text such as 'a', 'the', etc.
cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.transcript)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index
data_dtm
#print(data_dtm)

# Let's pickle it for later use
data_dtm.to_pickle(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\dtm.pkl')
# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
data_clean.to_pickle(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\data_clean.pkl')
pickle.dump(cv, open(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\cv.pkl', "wb"))
#---------------------------------------------- till now we saw cleaning the data -------------------------------------------------------------------

# -------------------------Now we will take a look on EDA (Exploratory Data Analysis ) -----------------------------------------------------------------
# using machines learning (ML) techniques, ew are going to find 
# 1.	Most common words - find these and create word clouds
# 2.	Size of vocabulary - look number of unique words and also how quickly someone speaks
# 3.	Amount of profanity - most common terms
# Read in the document-term matrix
data = pd.read_pickle(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\dtm.pkl')
#print(data)
data = data.transpose()
#print(data)
a = data.head()
#print(a)

# Find the top 5 words said by comedian
top_dict = {}
for c in data.columns:
    top = data[c].sort_values(ascending=False).head(5)
    top_dict[c]= list(zip(top.index, top.values))
top_dict
#print(top_dict)

# Print the top 5 words said by each comedian
for comedian, top_words in top_dict.items():
    print(comedian)
    print(', '.join([word for word, count in top_words[0:6]]))
    print('---')

# Let's first pull out the top 5 words for each comedian
words = []
for comedian in data.columns:
    top = [word for (word, count) in top_dict[comedian]]
    for t in top:
        words.append(t)
words
#print(words)

# Let's aggregate this list and identify the most common words along with how many routines they occur in
a = Counter(words).most_common()
#print(a)
# If more than half of the comedians have it as a top word, exclude it from the list
#add_stop_words = [word for word, count in Counter(words).most_common() if count > 1]
add_stop_words = [word for word, count in Counter(words).most_common() if count == 1] # for ali common words are  ['like', 'im', 'know', 'just', 'dont']
#print(add_stop_words)

# Let's update our document-term matrix with the new list of stop words
# Read in cleaned data
data_clean = pd.read_pickle(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\data_clean.pkl')
#print(data_clean.index()) #builtins.TypeError: 'Index' object is not callable
# Add new stop words
stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words) # text is imported from sklearn.feature_extraction library/module
#print('stop words are:-'+str(stop_words))
#for a in stop_words:
#    print(a)
    
# Recreate document-term matrix
cv = CountVectorizer(stop_words=stop_words) # CountVectorizer imported from sklearn.feature_extraction.text 
data_cv = cv.fit_transform(data_clean.transcript)
data_stop = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_stop.index = data_clean.index

# Pickle it for later use
pickle.dump(cv, open(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\cv_stop.pkl', "wb"))
data_stop.to_pickle(r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\dtm_stop.pkl')

# Let's make some word clouds!
#wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
#               max_font_size=150, random_state=42)
wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               width=480, height=480, margin=0)
# Reset the output dimensions
#plt.rcParams['figure.figsize'] = [16, 6]
#plt.rcParams['figure.figsize'] = [10,2]
plt.rcParams['figure.figsize'] = [10, 6]

full_names = ['Ali Wong']

# Create subplots for each comedian
for index, comedian in enumerate(data.columns):
    wc.generate(data_clean.transcript[comedian])
    
    #plt.subplot(3, 4, index+1) # subplot is to show the image inside the main graph, index is to align based on number.
    #plt.subplot(3, 4, index+2) 
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(full_names[index])
    
plt.show()
