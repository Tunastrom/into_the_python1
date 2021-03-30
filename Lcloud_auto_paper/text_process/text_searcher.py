import re

def text_searcher(needdatas_set, contents_str, pattern):
    seeing_str = contents_str
    r = re.compile(pattern)
    search_result = r.search(seeing_str).group()
    needdatas_set.add(search_result)
     
    