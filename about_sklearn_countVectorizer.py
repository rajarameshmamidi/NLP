from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
#print(vectorizer.vocabulary_) # output is {'the': 7, 'quick': 6, 'brown': 0, 'fox': 2, 'jumped': 3, 'over': 5, 'lazy': 4, 'dog': 1}
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
#print(vector.shape) # output is (1, 8)
#print(type(vector)) # output is <class 'scipy.sparse.csr.csr_matrix'>
print(vector.toarray())  # output is [[1 1 1 1 1 1 1 2]] 
