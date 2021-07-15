HEX = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

while alphabet := input().upper():
    if alphabet.isalpha() is False \
    or alphabet in HEX is False:
        continue
    print(f'입력 값: {alphabet, HEX[alphabet]}')
    break

for number in range(1,16):
    print(f'{format(HEX[alphabet], "X")}*{number}={format(HEX[alphabet]*number, "X")}')