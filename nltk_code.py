# Below code explains  how to access text corpus with Gutenderg

from nltk.corpus import gutenberg
#a = nltk.corpus.gutenberg.fileids() # to get in-built .txt files of gutenberg
#print(a) # output:- ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']

# i choose autsen-emma.txt book for practice  
#emma = nltk.corpus.gutenberg.words('austen-emma.txt') # nltk.corpus.gutenberg.words used to split the words in a file.
#emma = gutenberg.words('austen-emma.txt') # nltk.corpus.gutenberg.words used to split the words in a file.
#a=len(emma) # lenght used to find total words in the file. output(192427)
#print('total number of words in austen-emma.txt are:- %s'%(a))
file = 'my_text_file.txt'
text = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk'+'/' + file
#num_char = gutenberg.raw('austen-emma.txt')
#num_words = gutenberg.words(text)
#print('total number of words in my_text_file.txt are:- %s'%(len(num_words)))
num_letters = gutenberg.raw(text) # gutenberg.raw used to find number of letters/characters present in a file.
print('total number of letters used in my_text_file.txt are :- %s' %(len(num_letters)))
num_words = gutenberg.words(text)# gutenberg.word used to find number of words present in a file.
print('total number of words in %s are:- %s' %(file, len(num_words)))
num_sent = gutenberg.sents(text) # gutenberg.sents used to find number of sentences present in a file.
print('total number of sentences in %s are:- %s' %(file, len(num_sent)))
#--------------------------------------------------------------------------
#Note:- vocablary is nothing but words in a file. A file may have duplicate words.
#so, get distinct vocablaryies/words from a file we use set key word.
#--------------------------------------------------------------------------
num_vocab = len(set(w.lower() for w in gutenberg.words(text)))
print('total number of vocablaries in %s are:- %s' %(file, (num_vocab)))
a = len(num_letters)/len(num_words)
print('average number of letters used in a word are :- %s' %(a))
a = (num_vocab)/len(num_sent)
print('average number of words used in a sentence are :- %s' %(a))



'''
# different way's to get total count of list items in python
count = 0
for i in a:
    count +=1
print(count) # gives total count of list items.
#for no,in in enumerate(a):
#    print('%s ... %s'%(no,i)) # display's serial number with list item 
'''


#from nltk.book import * # To import all books available in nltk module
#a = text1
#a = text3.generate(10)
#print(a)

#import nltk
#text = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\my_text_file.txt'
#f = open(text,'r')
#raw =f.read()
#tokens= nltk.word_tokenize(raw) # word_tokenize will split the words in a sentence with comma seperated.
#print(tokens)
# To know common used words in a context, we use FreDist(frequency Distribution) key word.which is inbuilt in NLTK
#fdist1 = nltk.FreqDist(tokens)
#print(fdist1) # FreqDist with 48 samples and 947 outcomes is the output
# below command is to find 3 most common words used in the file. 
#a = fdist1.most_common(3)
#print('3 most commonly used words are:- %s' %a) # output :- 3 most commonly used words are:- [('.', 10), ('the', 10), (',', 9)]
#a = tokens.index('NLP')
#print('index of - it in the file is :-%s' %a)
#a = 100*tokens.count('it') / len(tokens)
#print('%s percentage of the text is taken up by a specific word'%a)
#a = tokens.count('it') # count function used to find how many time a word used. 
#print('%s used in the file' %a)
#a = len(tokens) # length(len) used to find words and punctuation symbols, or "tokens." A token is the technical name for a sequence of characters — such as hairy, his, or :) 
#print('contains of %s  words,punctuations and symbols or tokens  in % s'%(a,text))
#a = len(set(tokens)) # we can eliminate duplicates using set function 
#print('contains of %s distinct words,punctuations and symbols or tokens  in % s'%(a,text))
#mytext = nltk.Text(tokens) # Text used to return as text/word from a sentence.
#for words in mytext:
#    print(words)
#mytext.common_contexts(['might']) # common_contexts will display the start and end words in sentance(ex:- you_like, here might word is used between you and like of a sentence. 
#mytext.concordance('in')   # concordance used to search particular word in context of a file.
#mytext.similar('like')
#mytext.dispersion_plot(['Hi','in']) # dispersion_polt generates a graph to dispaly position infromation of a word present in a context of a file. numpy and Matplotlib packages need to install.
