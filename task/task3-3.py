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

print(list(lowercase_txt))