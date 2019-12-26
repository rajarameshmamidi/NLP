# Read in the corpus, including punctuation!
import pandas as pd
#Build a Markov Chain Function
from collections import defaultdict
#Create a Text Generator
import random

data = pd.read_pickle('corpus.pkl')
data

# Extract only Ali Wong's text
ali_text = data.transcript.loc['ali']
ali_text[:200]
print('data till index 200 is:- '+ali_text[:200])
#Build a Markov Chain Function
def markov_chain(text):
    '''The input is a string of text and the output will be a dictionary with each word as
       a key and each value as the list of words that come after the key in the text.'''
    
    # Tokenize the text by word, though including punctuation
    words = text.split(' ')
    
    # Initialize a default dictionary to hold all of the words and next words
    m_dict = defaultdict(list)
    
    # Create a zipped list of all of the word pairs and put them in word: list of next words format
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    m_dict = dict(m_dict)
    return m_dict
# Create the dictionary for Ali's routine, take a look at it
ali_dict = markov_chain(ali_text)
ali_dict
print('ali text info is:- '+str(ali_dict))

#Create a Text Generator
def generate_sentence(chain, count=15):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''

    # Capitalize the first word
    word1 = random.choice(list(chain.keys()))
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count-1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2

    # End it with a period
    sentence += '.'
    return(sentence)
a = generate_sentence(ali_dict)
print('random sentence:-'+a)