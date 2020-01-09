#-----------------------------------------------------------------------------------
# Basic sentiment analysis with nltk, numpy
# reading words of reviews.csv and match with words_positve.csv and word_negative.csv
# printing avarage sentiment of each review. either positive or negative
# we follow below rules / logic for positive or negative
'''    
    +1 * +1 = +1  very good = (positve)
    -1 * -1 = +1  not bad   = (positive)
    -1 * +1 = -1  not good  = (negative)
'''
#-----------------------------------------------------------------------------------
import csv
import numpy as np
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

# file path
review_file_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\sentiment_analysis_udyme\datasets\reviews.csv'
neg_words_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\sentiment_analysis_udyme\datasets\words-negative.csv'
pos_words_path = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\sentiment_analysis_udyme\datasets\words-positive.csv'

# reading all negative words from word_negative.csv and appendign to a list
negative = []
with open(neg_words_path,'r', encoding='utf-8') as neg_file:
    read = csv.reader(neg_file)
    for row in read:
        negative.append(row)

# reading all positive words from word_positive.csv and appendign to a list
positive = []
with open(pos_words_path,'r', encoding='utf-8') as pos_file:
    read = csv.reader(pos_file)
    for row in read:
        negative.append(row)

# displaying few negative and positive words which read from the files
'''print('negative words are:- %s' %(negative[:10]))
print('----------------------------------------------')
print('positive words are:- %s' %(positive[:10]))'''

'''
# creating a function to predict the sentiment of a text passed to it
def sentiment(text):
    text_sen = sent_tokenize(str(text)) # tokenie to sentence
    for sentence in text_sen: # we are passing each sentence and check how many time positive and negative words are there.
        #print(sentence)
        n_count = 0
        p_count = 0
        sent_words = word_tokenize(sentence) # tokenizing the sentence to words
        #print(sent_words)
        for word in sent_words:   # now we will pass each word of sentence and check if it is positive or negative
            for item in positive:
                if word == item[0]:
                    p_count +=1  # counting the positive words
                    #print('positive word in the sentence is:- %s' %(word))
            for item in negative:
                if word == item[0]:
                    n_count +=1  # counting the negative words 
                    #print('negative word in the sentence is:- %s' %(word))
        # now applying the logic / rules to predict the sentiment
        if(p_count > 0 and n_count == 0):
            print('positive sentence:-  '+ sentence)
        elif(n_count % 2 > 0):  # if odd number's then negative
            print('negative sentence:- '+ sentence)
        elif(n_count % 2 ==0 and n_count >0): # if even number then positive
            print('positive sentence:-  '+ sentence)
        else:
            print('nutral sentence:-  '+ sentence)

# caling the function by passing text
#sentiment('it was terribly bad.') # output :- negative sentence:- it was terribly bad.
#sentiment(' it is very good.') # output:- positive sentence:-   it is very good.
sentiment(' it is good.') # output:- negative sentence:-  it is good.
#sentiment(' Actually, it is not bad.') # output:- positive sentence:-   Actually, it is not bad.
#sentiment('this sentence about nothing') # output:- nutral sentence:-  this sentence about nothing
'''
# creating a function to predict the sentiment of a text passed to it
def sentiment(text):
    temp =[]
    text_sen = sent_tokenize(str(text)) # tokenie to sentence
    for sentence in text_sen: # we are passing each sentence and check how many time positive and negative words are there.
        #print(sentence)
        n_count = 0
        p_count = 0
        sent_words = word_tokenize(sentence) # tokenizing the sentence to words
        #print(sent_words)
        for word in sent_words:   # now we will pass each word of sentence and check if it is positive or negative
            for item in positive:
                if word == item[0]:
                    p_count +=1  # counting the positive words
                    #print('positive word in the sentence is:- %s' %(word))
            for item in negative:
                if word == item[0]:
                    n_count +=1  # counting the negative words 
                    #print('negative word in the sentence is:- %s' %(word))
        # now applying the logic / rules to predict the sentiment
        if(p_count > 0 and n_count == 0):
            temp.append(1) # appending if sentence is positive
        elif(n_count % 2 > 0):  # if odd number's then negative
            temp.append(-1) # appending if sentence is negative
        elif(n_count % 2 ==0 and n_count >0): # if even number then positive
            temp.append(1) # appending if sentence is positive
        else:
            temp.append(0) # appending if sentence is nutral
    return temp


# caling the function by passing text
comments = []
with open(review_file_path,'r', encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row)
# Now we will average the review od sentence with np.average
for review in comments:
    print('\n')
    print(np.average(sentiment(str(review))))
    print(review)
    
    ''' output of reviews below
    -0.2
["This camera is perfect for an enthusiastic amateur photographer. The pictures are razor-sharp, even in macro. It is small enough to fit easily in a coat pocket or purse. It is light enough to carry around all day without bother. Operating its many features is easy and often obvious - i'm no annie lebovitz, but i was able to figure out most of its abilities just messing around with it at a camera store. The manual does a fine job filling in any blanks that remain. The auto-focus performs well, but i love having the 12 optional scene modes - they are dummy-proof, and correspond to many situations in which i would actually seek to use the camera. Comes with a 16 mb compact flash and one rechargeable battery the charging unit, included, is fast and small. I bought a 256 mb cf and a second battery, so it's good to go on a long vacation. I enthusiastically recommend this camera."]


-0.375
["I got my camera three days back, and although i had some experience with digital cameras prior to purchasing this one, i still rate myself as a beginner. I bought this camera because it fit my budget and the pre-production and production model reviews were positive. It's easy to use, and yet very feature rich. In the auto mode it functions basically as a point and click, the scene modes are very easy to use and produce good results. The manual mode is feature rich and i can't wait to get the hang of it. The macro mode is exceptional, the pictures are very clear and you can take the pictures with the lens unbelievably close the subject. The battery life is very good, i got about 90 minutes with the lcd turned on all the time, the first time around, and i have been using it with the lcd off every now and then, and have yet needed to recharge it. The camera comes with a lexar 16mb starter card, which stores about 10 images in fine mode at the highest resolution, i intend to buy a bigger card soon."]


-0.6666666666666666
['I love photography. I had an older camera that was simply a point and shoot camera. I needed something with more power, so i bought a nikon coolpix 4300. I fell in love with this camera, it combines ease of use, with an immense amount of options and power. You can use the scene modes, or fine tune the options, i. you can change the iso level, shutter speed, etc. This camera is ideal for people who want more power, but don’t want to spend 1000s dollars on a camera. ']


-0.36363636363636365
["I bought coolpix 4300 two months after i had bought canon powershot s400. It was not easy sharing one with my teen age kid. The two cameras are very similar in functionality and pricing. I've had no problem with canon whatsoever. With nikon, although picture qualities are as good as any other 4 mp cameras, i've had the following headaches. Pictures won't transfer to pc directly from the camera using the included transfer cable. I did everything i could, and it took many days of frustration before concluding that the only way to transfer to pc is with the card reader. The speed is noticeably slower than canon, especially so with flashes on. With low battery, it twice wiped out the entire pictures in the memory chip. I used lexar 256 mb and i still use it which means nothing is wrong with lexar. Be very careful when the battery is low and make sure to carry extra batteries. "]


-0.42857142857142855
['The other reviewers have clearly pointed all the good things about this camera, which i do agree. But there are certain issues might be they are to me here - all of them are minor; not major ones though. This camera keeps on autofocusing in auto mode with a buzzing sound which can\'t be stopped. Would be really good if they have given an option to stop this autofocusing. If you want to have the date; time on the image, its only through their software "nikon view" which reads the images date; time from the images meta-data. So if you use your card reader; copy images - you got to once again open them through their software to put the date; time. In that too, there is not a direct way to add date; time - you got to say\' print images\' to a different directory in which there is an option to specify the date; time. Even the slightest of the shakes totally distorts your image. Images taken indoor were not so clear. You got to have flash on to get it even though your room is well lit. Lens cap is a really annoying. The movie clips taken will always have some noise in it, you can\'t avoid that. But overall this is a good camera with a\' really good\' picture clarity; an exceptional close-up shooting capability. I would rate this is 4.5 stars picture quality; image size defined above are specific to nikon coolpix.']


0.5714285714285714
["Within a year, there are problems with my menu dial knob. It became stuck which makes it almost impossible to switch between modes. I send my camera to nikon for servicing, took them a whole 6 weeks to diagnose the problem. Worse of all, they claim that it's some kind of internal damage and refuse to cover the cost via warranty! They wouldn't repair my camera unless if i pay $100 for parts? and labor! It is a good camera in terms of the function and quality, but take your chance with it because nikon absolutely sucks when it comes to customer service."]


0.0
['Got a "system error" problem 30 days after purchase. Made the camera totally inoperable. Also, the lens cap design is flawed. You have to manually Audio on video also lacking. Otherwise, it takes very good pictures; shutter delay is not so bad either. Still, had to send it back to nikon for repair.']


0.09090909090909091
['I am an amateur photographer and here is a piece of advise to all the folks who are thinking about making a move the digital world. I feel, is the best camera out there for the features and price. I had initially thought of buying a 2 or 3 megapixel camera but these are good for 4x6" or 5x7" prints and i wanted some really great 8x10" photos once in a while. I did not want a very small camera as it seems to get lost in my hands and i was not comfortable with that. I wanted a decent sized camera with a contour for my fingers to hold it steadily. I wanted a camera that had a lot of built-in settings for different types of surroundings while giving me an option to use my photography skills although, I am an amateur with an interest in photography by turning on the manual settings. I wanted a respected brand and had to stay within my budget because i had bought an expensive camcorder before but had not used it much. Depending on all the above requirements, I had narrowed down my search to nikon 4300 and canon powershot s400 models. Nikon got the final nod for its settings auto and manual along with movie modes, medium; compact size, price, brand name, good software that is included and previous reviews. I should say I have been very happy with my decision ever since. The pictures are absolutely amazing - the camera captures the minutest of details.']

    '''

#sentiment('it was terribly bad.') # output :- negative sentence:- it was terribly bad.
#sentiment(' it is very good.') # output:- positive sentence:-   it is very good.
#sentiment(' it is good.') # output:- negative sentence:-  it is good.
#sentiment(' Actually, it is not bad.') # output:- positive sentence:-   Actually, it is not bad.
#sentiment('this sentence about nothing') # output:- nutral sentence:-  this sentence about nothing