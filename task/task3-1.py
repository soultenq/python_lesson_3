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

print(stripped_text)
#print (dd)
#print(string.punctuation)

