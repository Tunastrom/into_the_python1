import time

year = time.strftime('%Y',time.localtime(time.time()))
month = time.strftime('%x',time.localtime(time.time()))
hours = time.strftime('%X',time.localtime(time.time())) 
print(year+'/'+month[0:5], hours)