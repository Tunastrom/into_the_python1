import re, math

# with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102.txt', 'r') as f: 
#     text = f.read()
text = ''
# pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
pattern = '[\d]+[inc]'
r = re.compile(pattern)
print(dir(r))
search_result = r.search(text).group()
print(search_result)

# while search_result: 
#     replaced_result = search_result.replace(' ','')
#     text = text.replace(search_result,replaced_result)
#     search_result=r.search(text).group()
        

# test_str = '2021. 2. 26 오후 2:06:00'
# pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
# result = re.search(pattern, test_str)
# result= result.group().replace(' ','')

# print(result)
