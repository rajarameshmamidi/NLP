# Below code explains about slicing in python
sent = ['word1', 'word2', 'word3', 'word4', 'word5','word6', 'word7', 'word8', 'word9', 'word10']
a = sent[0]
print(a)
b = sent[9]
print(b)
c =sent[5:8]
print(c)
d = sent[:3]
print(d)
text = r'C:\Users\rrmamidi\Desktop\to windows 10\compress_1\python\meachin learning doc\About nltk\my_text_file.txt'
e=text[:3]
print(e)
file= open(text,'r')
a = file.read()
f =a[:10]  # will return 0 -9 letters.
print(f)

