f1 = open('C:/doit/test.txt', 'r')
contents = f1.read()
contents = contents.replace('java','python')
f1.close()

f2 = open('C:/doit/test.txt', 'w')
f2.write(contents)
f2.close()ggqqpp