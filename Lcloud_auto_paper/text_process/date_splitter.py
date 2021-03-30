import re,os

def date_splitter(pattern,string):
    split_str = string
    #print(pattern)
    r = re.compile(pattern)
    search_result = r.search(split_str).group()
    while search_result:
        # print(search_result)
        replaced_result = search_result.replace(' ','')
        split_str = split_str.replace(search_result,replaced_result)
        try:
            print('날짜 공백 제거 중')
            os.system('cls')
            search_result=r.search(split_str).group()
        except:
            search_result = False
    
    return split_str





