import re, math, datetime, random

# with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102.txt', 'r') as f: 
#     text = f.read()

rubbish_list = {'tran', 'inc', 'arc'} 

text = '2021.1.23오전1:00:00' 
# print(text)
pattern = '\d+'
# pattern = '[]+'
r = re.compile(pattern)
year, month, day = '', '', ''
for i in range(len(text)):
    if year != '' and month != '' and day != '':
        break
    search_result = r.search(text).group()
    if i == 0:
        year = search_result
        text = text.replace(search_result,'')
    if i == 1:
        month = search_result
        text = text.replace(search_result,'')
    if i == 2:
        day = search_result
        text = text.replace(search_result,'')

print('year, month, day: {}, {}, {}'.format(year, month, day))
     

# search_result = False

# for search_this in rubbish_list:
#     print(text.find(search_this))
#     if text.find(search_this) != -1:
#        search_result = True
#        break

print(search_result)

# datetime.date()



# while search_result: 
#     replaced_result = search_result.replace(' ','')
#     text = text.replace(search_result,replaced_result)
#     search_result=r.search(text).group()
        

# test_str = '2021. 2. 26 오후 2:06:00'
# pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
# result = re.search(pattern, test_str)
# result= result.group().replace(' ','')

# print(result)

random.randint()
