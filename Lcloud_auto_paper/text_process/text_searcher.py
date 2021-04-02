import re

def text_searcher(string, pattern):
    seeing_str = string
    r = re.compile(pattern)
    search_result = r.search(seeing_str).group()
    return search_result 
    
    