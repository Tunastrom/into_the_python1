# 기존
import os, secrets, random
print(os.getrandom(19))
print(os.urandom(19))
print(secrets.token_bytes(19))
# -> 다시 생성 불가

print(random.randbytes(19))
