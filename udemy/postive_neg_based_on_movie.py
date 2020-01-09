# Building a model to classify movie reviews
import numpy as np
import pandas as pd



file_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\sentiment_analysis_udyme\datasets\moviereviews.tsv'
df = pd.read_csv(file_path, sep = '\t') 
print(df.head())
print(len(df))
df.isnull().sum()
#we can remove space or 'NAN' or empty row as below
df.dropna(inplace = True)
df.isnull().sum()
#print(df['review'][0])
#print(df['review'][2])
'''
checking for empty space
mystring = 'hello'
empty = ' '
print(mystring.isspace())
print(empty.isspace())

'''
# checking empty space from the movie review data
blanks = []
# (index, label, review text)
for i,ld, rv in df.itertuples():
    if  rv.isspace():
	    blanks.append(i)
df. drop(blanks, inplace=True)
len(df)

# spliting the data
from sklearn.model_selection import train_test_split
X = df['review']
y = df['label']
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 42)

# creatinf pipeline
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
text_clf = Pipeline([('tfidf',TfidfVectorizer()), ('clf',LinearSVC())])
text_clf.fit(X_train,y_train)
prediction = text_clf.predict(x_text)

# finding score
from sklearn.metrics import confusion_matrix, classification_score, accuracy_score
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
print(accuracy_score(y_test, prediction))

