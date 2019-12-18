#------------------------------------------------------------------
#In this porgram, I will explain how to create a language model for 
#generating natural language text by implement and training state-of-the-art 
#Recurrent Neural Network. I will use python programming language for this purpose. 
#The objective of this model is to generate new text, given that some input text is present. Lets start building the architecture.
#------------------------------------------------------------------

# Importing keras & numpy module
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
#from keras.models import Sequential
from tensorflow.keras.models import Sequential, load_model
import keras.utils as ku 
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#There will be three main parts of the code: dataset preparation, model training,
#and generating prediction. The boiler plate code of this architecture is following:

#In dataset preparation step, we will first perform Tokenization. 
#Tokenization is a process of extracting tokens (terms / words) from a corpus. 
#Python’s library Keras has inbuilt model for tokenization which can be used to obtain the tokens and their index in the corpus.

tokenizer = Tokenizer()
def dataset_preparation(data):
    corpus = data.lower().split("\n") 
    #print('input word in different way :- %s' %(corpus))
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1
    #print('total_words are %s'% total_words)
    #Next, we need to convert the corpus into a flat dataset of sentence sequences.
    input_sequences = []
    for line in corpus:
        #print('lines are :- %s' %(line))
        token_list = tokenizer.texts_to_sequences([line])[0]
        #print('token_list are:- %s' %token_list)
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            #print('n_gram_sequence are %s' %n_gram_sequence)
            input_sequences.append(n_gram_sequence)    
    #Now that we have generated a data-set which contains sequence of tokens, 
    #it is possible that different sequences have different lengths. Before 
    #starting training the model, we need to pad the sequences and make their lengths equal.
    #We can use pad_sequence function of Kears for this purpose.
    max_sequence_len = max([len(x) for x in input_sequences])
    #print('max_sequence_len is %s' %(max_sequence_len))
    # NOTE:- Array will build based on max number of words in a line. in this example we have 5 words as max. 
    input_sequences = np.array(pad_sequences(input_sequences,   
                              maxlen=max_sequence_len, padding='pre')) 
    #print('padding input_sequences %s' %(input_sequences))
    #To input this data into a learning model, we need to create predictors and label.
    #We will create N-grams sequence as predictors and the next word of the N-gram as label.
    #Lets write the code for the same
    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
    #print('predictors are:- %s'%predictors)
    #print('label are:- %s' %(label))
    label = ku.to_categorical(label, num_classes=total_words)  
    #print('label after keras are:- %s' %(label)) 
    return predictors, label, max_sequence_len, total_words
#now we can obtain the input vector X and the label vector Y which can be used 
#for the training purposes. Recent research experiments have shown that 
#recurrent neural networks have shown a good performance in sequence to sequence 
#learning and text data applications. Lets look at them in brief.    
def create_model(predictors, label, max_sequence_len, total_words):
    input_len = max_sequence_len - 1
    model = tf.keras.Sequential()
    model.add(Embedding(total_words, 10, input_length=input_len))
    model.add(layers.LSTM(150, return_sequences = True))
    #model.add(Dropout(0.1))
    model.add(layers.Dense(total_words, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    earlystop = EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')
    model.fit(predictors, label, epochs=100, verbose=1, callbacks=[earlystop])
    return model
#our model architecture is now ready and we can train it using our data. 
#Next lets write the function to predict the next word based on the input words (or seed text).
#We will first tokenize the seed text, pad the sequences and pass into the trained model to get predicted word.
#The multiple predicted words can be appended together to get predicted sequence.    
def generate_text(seed_text, next_words, max_sequence_len, model):
    for j in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen= 
                             max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
  
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text
    
text = '''They put on their mittens,
This is raja'''
predictors, label, max_len, total_words = dataset_preparation(text)
print('value of x:- %s' %(predictors))
print('value of y:- %s' %(label))
print('value of max_len:- %s' %(max_len))
print('value of total_words:- %s' %(total_words))
model = create_model(predictors, label, max_len, total_words)
print('model is: %s' %(model))