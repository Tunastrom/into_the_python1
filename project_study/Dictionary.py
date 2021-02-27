dic = {1:"My", 2:"Name", 3:"Is",4:"Python"}
print(dic[1])
print(dic[2])
print(dic[3])
print(dic[4])

dic_keys=dic.keys()
dic_in_keys=3 in dic.keys()
dic_value=dic.values()
dic_items=dic.items()

print(dic_keys) # return list
print(dic_in_keys) #return boolean
print(dic_value) # return list of values
print(dic_items) # return list of key-value pairs

print(type(dic_keys))
print(type(dic_in_keys))
print(type(dic_value))
print(type(dic_items))