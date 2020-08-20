import string
file = open('text.txt','r')
text = file.read()

dd = dict.fromkeys(string.punctuation)
dd['»']=None
dd['«']=None
dd['—']=None
dd['-']=None

transmap = str.maketrans(dd)
stripped_text = text.translate(transmap)

lowercase_txt=map(str.lower, stripped_text.split())

list_text=list(lowercase_txt)

count=dict()

for word in list_text:
    count[word] = count.get(word,0) + 1

five_words = sorted(count.items(), key=lambda x: x[1], reverse=True)

print(five_words[0:5])

print(len(five_words))
