# Below code demonstrates about sentiment analysis of words
# We'll start by reading in the corpus, which preserves word order
from textblob import TextBlob  #Linguistic researchers have labeled the sentiment of words based on their domain expertise. Sentiment of words can vary based on where it is in a sentence. The TextBlob module allows us to take advantage of these labels.
import matplotlib.pyplot as plt
import pandas as pd
pkl_file=r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\adashofdata\pickel\corpus.pkl'
data = pd.read_pickle(pkl_file)
data
#print(data)
# Create quick lambda functions to find the polarity and subjectivity of each routine
pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

# here apply() is pandas funcation
data['polarity'] = data['transcript'].apply(pol)
data['subjectivity'] = data['transcript'].apply(sub)
data

# Let's plot the results
plt.rcParams['figure.figsize'] = [10, 8]
for index, comedian in enumerate(data.index):
    x = data.polarity.loc[comedian]
    y = data.subjectivity.loc[comedian]
    plt.scatter(x, y, color='blue')
    plt.text(x+.001, y+.001, data['full_name'][index], fontsize=10)
    plt.xlim(-.01, .12) 
    
plt.title('Sentiment Analysis', fontsize=20)
plt.xlabel('<-- Negative -------- Positive -->', fontsize=15)
plt.ylabel('<-- Facts -------- Opinions -->', fontsize=15)

#plt.show()

#Instead of looking at the overall sentiment, let's see if there's anything interesting about the sentiment over time throughout each routine.
# Split each routine into 10 parts
import numpy as np
import math
def split_text(text, n=10):
    '''Takes in a string of text and splits into n equal parts, with a default of 10 equal parts.'''

    # Calculate length of text, the size of each chunk of text and the starting points of each chunk of text
    length = len(text)
    print('length is:- '+str(length))
    size = math.floor(length / n)
    print('size is:- '+str(size)) 
    start = np.arange(0, length, size)
    print('start is:- %s' %(start))
    # Pull out equally sized pieces of text and put it into a list
    split_list = []
    for piece in range(n):
        split_list.append(text[start[piece]:start[piece]+size])
    print('split_list is:- '+str(split_list))
    return split_list

# Let's take a look at our data again
data

# Let's create a list to hold all of the pieces of text
list_pieces = []
for t in data.transcript:
    split = split_text(t)
    list_pieces.append(split)

list_pieces    
# The list has 10 elements, one for each transcript
len(list_pieces)
print(len(list_pieces))
# Each transcript has been split into 10 pieces of text
print(len(list_pieces[0]))

# Calculate the polarity for each piece of text

polarity_transcript = []
for lp in list_pieces:
    polarity_piece = []
    for p in lp:
        polarity_piece.append(TextBlob(p).sentiment.polarity)
    polarity_transcript.append(polarity_piece)
    
polarity_transcript
print(polarity_piece)
# Show the plot for one comedian
plt.plot(polarity_transcript[0])
plt.title(data['full_name'].index[0])
#plt.show()
