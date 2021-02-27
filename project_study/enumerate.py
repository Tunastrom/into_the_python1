for i, name in enumerate(['body', 'foo', 'bar']): # return enumerate object  
    print(i, name)

names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1 ,name))