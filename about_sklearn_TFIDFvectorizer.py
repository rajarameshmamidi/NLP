from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog.",
		"The dog.",
		"The fox"]
# create the instance transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
#print(vectorizer.vocabulary_) # output is {'the': 7, 'quick': 6, 'brown': 0, 'fox': 2, 'jumped': 3, 'over': 5, 'lazy': 4, 'dog': 1}
#print(vectorizer.idf_) # output is [1.69314718 1.28768207 1.28768207 1.69314718 1.69314718 1.69314718 1.69314718 1.        ]
# encode document
#vector = vectorizer.transform([text[0]]) 
vector = vectorizer.transform([text[1]])  # output is [[0.         0.78980693 0.         0.         0.         0.  0.         0.61335554]]
# summarize encoded vector
#print(vector.shape) # output is (1, 8)
print(vector.toarray()) # output is [[0.36388646 0.27674503 0.27674503 0.36388646 0.36388646 0.36388646 0.36388646 0.42983441]]