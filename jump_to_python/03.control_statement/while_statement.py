prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

## 프롬프트 ##
number = 0
while number != 4:
    print(prompt)
    number = int(input())


## 1부터 10까지 숫자중 홀수만 ##

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

