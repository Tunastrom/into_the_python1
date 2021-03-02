
a = {1:'a'}
a['name'] ='pey'
print(a)

a['test'] =[1,2,3]
print(a)

# 동일 키값 입력시 기존 것 삭제
a[1] = 'b'
print(a)

# key값 리스트 불가
# b={[1,2] : 'hi'}
# print(b)

## 딕셔너리 관련 함수##

a = {'name': 'pey', 'phone':'0119993323','birth':'1118'}

# keys()
print(a.keys()) #dict-keys 객체(iterable) 반환 -> list보다 메모리 덜씀
print(list(a.keys())) #3.0이전 버전에서는 a.keys()가 list 반환

for k in a.keys():
    print(k)

# values()
print(a.values())

# items()
print(a.items()) ## list에 담은 tuple들 반환

# clear()
a.clear()
print(a)

a = {'name': 'pey', 'phone':'0119993323','birth':'1118'}

# get()

print(a.get("name"))
print(a.get('phone'))
print(a.get('nokey'))
# print(a.['nokey']) # 존재하지 않는 키 값 -> 오류
print(a.get('foo', 'bar')) # 값 없으면 디폴트 값 반환

#in()
print('name' in a)
print('email' in a)


