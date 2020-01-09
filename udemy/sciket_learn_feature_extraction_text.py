# Basic manual implementation of building a vocabulary
# using scikit-learn for vectorization
# using pipelines with scikit-learn
# working with message data directly
'''
vocab = {}
i = 1

with open('1.txt') as f: # also check for '2.txt' file
    x = f.read().lower.split()

for word in x:
    if word in vocab:
	   continue
	else:
	    vocab[word] = i
		i += 1
print(vocab)

one = ['1txt']+[0]* len(vocab)

with open('1.txt') as f:
    x = f.read().lower().split()
for word in x:
    two[vocab[word]]+= 1

two = ['2.txt']+[0]* len(vocab)

with open('2.txt') as f:
    x = f.read().lower().split()
for word in x:
    two[vocab[word]]+= 1	

# compare two vectors
print(f'{one} \ n {two}')
'''

from sklearn.model_selection import train_test_split
from sklearn.featrure_extraction.text import CountVectorizer
from sklearn.featrure_extraction.text import TfidfTransformer
from sklearn import metrics 
import numpy as np
import pands as pd
file_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\sentiment_analysis_udyme\datasets\smsspamcollection.tsv'
df = pd.read_csv(file_path, sep = '\t')
df.isnull().sum() # checking for null or empty or missing
df['label'].value_count()

# splitting the data
# X is feature data
X = df['message']# passing the text to X

y= df['label']

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 42)
'''
count_vect = CountVectorizer()
# Fit vectorizer to the data (build a vocab, count the number of words..)

count_vect.fit(X_train)
X_train_counts = count_vect.transform(X_train)

# Transform the original text message to vector
X_train_counts = count_vect.fit_transform(X_train)
#print(X_train_counts)
# print(X_train.shape)
#print(X_train_counts.shape)

tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(x_train_tfidf.shape)

# combination of CountVectorizer and TfidfTransformer is TfidfVectorizer
from sklearn.featrure_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
x_train_tfidf = vectorizer.fit_transform(X_train)
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
print(accuracy_score(y_test, prediction))

from sklearn.svm import LinearSVC

clf = LinearSVC()
clf.fit(x_train_tfidf,y_train)
prediction = clf.predict(X_test)
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
print(accuracy_score(y_test, prediction))
'''
# pipline is a combination of all TfidfTransformer, LinearSVC aslo to reduce line of code.
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf',LinearSVC())])
text_clf.fit(X_train,y_train) 
prediction = text_clf.predict(X_test)
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
print(accuracy_score(y_test, prediction))

# now we will check our model how it predicts by passing a raw text as below
text_clf.predict(['Hi how are you doing today.'])
text_clf.predict(['Congratulation! you have been selcted as a winner. Text to own 45568 prize money.'])