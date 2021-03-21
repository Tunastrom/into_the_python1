import re

with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102.txt', 'r') as f: 
    Contents_str = f.read() 
    pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
    search_result = re.search(pattern, Contents_str).group()
    print(search_result)
    while search_result:
        replaced_result = search_result.replace(' ','')
        Contents_str = Contents_str.replace(search_result,replaced_result)
        search_result=re.search(pattern, Contents_str).group()
        

# test_str = '2021. 2. 26 오후 2:06:00'
# pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
# result = re.search(pattern, test_str)
# result= result.group().replace(' ','')

# print(result)
