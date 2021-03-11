f = open('test.txt','r')

if f.read() == '': 
    d = open('test.txt','w')
    d.write('Life is too short\nyou need java')
    d.close()
    f = open('test.txt','r')
     
all_sentences = f.read()

new_sentences = all_sentences.replace('java','python')

f = open('test.txt','a')
f.writelines(new_sentences)
f.close()

v = open('test.txt','r')
print(v.read())