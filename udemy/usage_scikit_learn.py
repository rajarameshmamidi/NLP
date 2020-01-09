# using scikit_learn ovreview
# predict the given text is spam / ham based on length and punctuation columns  in file
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np
import pandas as pd
file_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\sentiment_analysis_udyme\datasets\smsspamcollection.tsv'

# getting informtaion of data using pandas
df = pd.read_csv(file_path, sep='\t')
df.head() 
df.isnull().sum() # checking null in the data and summing
len(df)
df['label'].unique()
df['label'].value_count()

# X is feature data
X = df[['length','punc']] # passing list of column['length','punc'] to df[] 

# y is our label
y = df['label']

# spliting the data to train and test
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 42)
print(X_train.shape()) # checking the shape (3900,2)
print(X_test.shape()) # checking the shape (1672,2)
print(y_train.shape()) # checking the shape (1672,)
print(y_test.shape()) # checking the shape ()

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
predection = lr_model.predict(X_test) # passing test data to our trained model to predict
print(metrics.confusion_matrix(y_test, predection), index = ['ham','spam'], columns=['ham','spam'])
'''
output:
[[1404 44]
 [ 219  5]
]
    ham    spam
ham 1404   44
spam  219   5
'''
print(metrics.classification_report(y_test, predection), index = ['ham','spam'], columns=['ham','spam'])

print(metrics.accuracy_score(y_test, predection))

'''
# predicting the output with MultinomialNB of naie_bayes
from sklearn.naive_bayes import MultinomialNB
nb_model = MultinomialNB()
nb_model.fit(X_train,y_train)
prediction = nb_model.predict(x_test)
print(metrics.confusion_matrix(y_test, predection), index = ['ham','spam'], columns=['ham','spam'])

# predicting the output with SVC of svm(support vector model)
from sklearn.svm import SVC
svc_model = SVC()
svc_model.fit(X_train,y_train)
prediction = nb_model.predict(x_test)
print(metrics.confusion_matrix(y_test, predection), index = ['ham','spam'], columns=['ham','spam'])
'''
