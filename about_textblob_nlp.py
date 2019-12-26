from textblob import TextBlob # Text analysis module
import pyttsx3 # test-to-speach module

blob = TextBlob("Analytics Vidhya is a great platform to learn data science. \n It helps community through blogs, hackathons, discussions,etc.")
print(blob.sentences) # output is:- [Sentence("Analytics Vidhya is a great platform to learn data science."), Sentence("It helps community through blogs, hackathons, discussions,etc.")]

# using text to speach module
for_speach = 'Now i am going to say about natural language processing text' + str(blob)
engine = pyttsx3.init()
#engine.say(blob)
# Set properties _before_ you add things to say
#engine.setProperty('rate', 50)    # Speed percent (can go over 100) it's too slow.
engine.setProperty('rate', 100)    # Speed percent (can go over 100) it's ok
#engine.setProperty('rate', 150)    # Speed percent (can go over 100) it's ok
#engine.setProperty('rate', 1500)    # Speed percent (can go over 100) it's too fast
#engine.setProperty('volume', 0.9)  # Volume 0-1
engine.say(for_speach)
engine.runAndWait()

'''
## printing words of particular sentence . below code is to dispaly words of first sentence
for words in blob.sentences[0].words:  
  print (words)

## printing words from give text
for words in blob.words:  
  print (words)

# Below code is to display nonu phrase
for np in blob.noun_phrases:
    print(np)
    
# Below code is to display Part-of-speech Tagging
for words, tag in blob.tags:
    print(words, tag)

#Sentiment Analysis
print(blob.sentiment) #output: - Sentiment(polarity=0.8, subjectivity=0.75)
'''
'''
#Translation and Language Detection
blob = TextBlob("Hello")
a=blob.detect_language()
print(a)
#a = blob.translate(to='te')
#print(a)
'''