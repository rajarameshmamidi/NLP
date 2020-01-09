# Below code is used to predict gender from list of values using Naive Bayes
# building the feature set base on last two letters of given name
# nltk provide list of male and female to train a model.
# P(A|B) = P(B|A) * P(A) / P(B)
# for example name given female ends with aeiouy and the naive Bayes formula look as below
# P(female|'[aeiouy]') = p('[aeiouy]'|female) P(female) / p('[aeiouy]')
import nltk
import random # used for random selection in our model
from nltk.corpus import names # importing male and female list from nltk
import matpoltlib.pypolt  as plt
matplotlib.style.use('ggplot')
a = names.fileids()
print(a)

# getting conditional frequency distribution from names.fileids and getting last two letter from the names
name_cfd = nltk.conditionalFreqDist((fileid,name[-2:]) for fileid in names.fileids() for name in names.words(fileid))

# now ploting the graph
plt.figure(figsize = (50,10))
name_cfd.plot() 

# build a function to get last two letters
def name_features(name):
    return {'pair' : name[-2:]}

# calling function

name_feature('katy') # output : {'pair' : 'ty'}

# using name_features custom function to build a dictionary of features from the names provided by nltk 
name_list = [(name,'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')]
#displaind first 10 names
print(name_list[:10]) 

#displaind last 10 names
print(name_list[-10:]) 

# now we will split our data names and genders into two sets traing(which will used find letter pairs in names and assinged genders) 
#and test set(we will use and give our model name wihtout genders and see how well it performs.)
# we will create training set and test set randomly
random.shuffle(name_list)
print(name_list[:10])

features = [(name_features(name), gender)for (name, gender) in name_list]
print(features[:10])

# we want to split this(features) list in half to train and test sets
# we train our model on last two letter and it's gone learn whether it is female or male 
# with testing test we give out model with last two letters without female or male indicator
# and guess  how well our model works with last two letters come from male or female

# spliting into half
len(features)/2

# spliting into train and test
training_set = features[:3972]
testining_set = features[3972:]

# using Naive bayes classifier to train our model
classifier = nltk.NavieBayesClassifier.train(training_set)

# getting original name list and check the gender exists or not
male_names = names.words('male.txt')
a = 'carmello' in male_names
print(a)

# using classifier model will see what the model thinks 'carmello' is? by passing to custome function. 
classifier.classify(name_feature('carmello'))

# now will see the accuracy of model with testing_set
a = nltk.classify.accuracy(classifier, testing_set)
print(a)









