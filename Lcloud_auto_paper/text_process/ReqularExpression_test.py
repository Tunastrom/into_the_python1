import re, math

# with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102.txt', 'r') as f: 
#     text = f.read()

rubbish_list = {'tran', 'inc', 'arc'} 

text = 'LCNCLD-DB-VSDB_mssql_inc'.lower() 
print(text)
# pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
# pattern = '[]+'
# r = re.compile(pattern)
# search_result = r.search(text).group()

search_result = False

for search_this in rubbish_list:
    print(text.find(search_this))
    if text.find(search_this) != -1:
       search_result = True
       break

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
