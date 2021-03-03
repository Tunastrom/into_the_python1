test_list =['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first,last)
    # 튜플이기 때문에 각각의 요소가 자동으로 first, last 변수에 매칭됨
    # 1~2개의 인수에만 가능
