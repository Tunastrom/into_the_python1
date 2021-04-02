import re,os

def date_splitter(pattern,string):
    split_str = string
    #print(pattern)
    r = re.compile(pattern)
    search_result = r.search(split_str).group()
    print('날짜 공백 제거 중')
    while search_result:
        # print(search_result)
        replaced_result = search_result.replace(' ','')
        split_str = split_str.replace(search_result,replaced_result)
        try:
            search_result=r.search(split_str).group()
        except:
            search_result = False
    os.system('cls')       
    
    return split_str





