# tf-idf mehtod to find important words from a document when we have collection of documents
# using this we can determin a documnet might be about if we have really large collection 
# and it is not fessble to access each of them and we can do example of this now.

import nltk
import math
# below files are shared by trainer
# another way to get the dataset files...this will reduce the lines of code

'''
dataset = {f'tfidf_{i}.txt': open(f'tfidf_{i}.txt').read() for i in range(1,11)}
'''

# one more way
'''for i in range(1,11):
    dataset['tfidf_%d.txt' %i] = open('tfidf_%d.txt' %i).read()
'''

dataset = {
    "tfidf_1.txt":open("tfidf_1.txt").read(),
    "tfidf_2.txt":open("tfidf_2.txt").read(),
    "tfidf_3.txt":open("tfidf_3.txt").read(),
    "tfidf_4.txt":open("tfidf_4.txt").read(),
    "tfidf_5.txt":open("tfidf_5.txt").read(),
    "tfidf_6.txt":open("tfidf_6.txt").read(),
    "tfidf_7.txt":open("tfidf_7.txt").read(),
    "tfidf_8.txt":open("tfidf_8.txt").read(),
    "tfidf_9.txt":open("tfidf_9.txt").read(),
    "tfidf_10.txt":open("tfidf_10.txt").read()
}
# check the data of the file with below
#print(dataset.keys())
#print(datset['tfidf_1.txt'])


# using TF(term frequecy function) we find number of times a words appears in given docuemnt
# Calculate term frequencies
def tf(dataset, file_name):
    text = dataset[file_name]
    tokens = nltk.word_tokenize(text) # tokenizing the words from the text
    fd = nltk.FreqDist(tokens) #
    return fd
# finding what is the frequency distribution (count of words) for 'tfidf_1.txt'	
 a = tf(dataset, 'tfidf_1.txt')
 #print(a)
 
# IDF to find number of documents that contains specific word out of all document we have.
# in this case we have 10 douments, and we want to look for word 'world' out of 10 documents.
# Calculate inverse document frequency
def idf(dataset, term):
    count = [term in dataset[file_name] for file_name in dataset]
    inv_df = math.log(len(count)/sum(count))
    return inv_df

# calling function
a = idf(dataset,'world')
#print(a)
	
	
# multiple tf and idf to get tfidf score	
def tfidf(dataset, file_name, n):
    term_scores = {}
    file_fd = tf(dataset,file_name)
    for term in file_fd:
        if term.isalpha():
            idf_val = idf(dataset,term)
            tf_val = tf(dataset, file_name)[term]
            tfidf_val = tf_val*idf_val
            term_scores[term] = round(tfidf_val,2)
    return sorted(term_scores.items(), key=lambda x:-x[1])[:n]

# calling function
a = tfidf(dataset,'tfidf_1.txt',10)
#print(a)

# now we will test for every single docuemnt
for file_name in dataset:
    print('{0}: \n {1} \n'.format(file_name,tfidf(dataset,file_name,5)))

