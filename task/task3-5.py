import string
import pymorphy2
file = open('text.txt','r')
text = file.read()
norm=[]

dd = dict.fromkeys(string.punctuation)
dd['»']=None
dd['«']=None
dd['—']=None
dd['-']=None

transmap = str.maketrans(dd)
stripped_text = text.translate(transmap)

lowercase_txt=map(str.lower, stripped_text.split())

morph = pymorphy2.MorphAnalyzer()

for i in lowercase_txt:
    p = morph.parse(i)[0]
    norm.append(p.normal_form)
    print(norm)
    print(len(norm))