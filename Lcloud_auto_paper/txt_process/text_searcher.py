import re

def text_searcher(string, pattern):
    seeing_str = string
    r = re.compile(pattern)
    search_result = r.search(seeing_str).group()
    return search_result

test_dict = {'Type': 1, 'Status': 2, 'Client': 5, 'JobPolicy': 3, 'JobSchedule': 4, 'StartTime': 0, 'Kilobytes': 6}
print(test_dict['StartTime'])
    
    