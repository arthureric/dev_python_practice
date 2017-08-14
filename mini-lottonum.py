

"""
로또번호 추출하기
: 범위내의 숫자들을 무작위로 원하는 횟수만큼 추출하기
"""
import random


#-----------------------------------------------------------------------------
"""
<아이디어 1 : randint범위내에서 random하게 여러개추출하기>
"""
print(random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45))

## 오류코드 Traceback (most recent call last):
#   File "C:\Users\user\dev\python_practice_w\dev_python_practice\mini-lottonum.py", line 8, in <module>
#     print(random.randint(1,45),
# NameError: name 'random' is not defined
## 해결 >> import random 했는지 체크할 것

#-----------------------------------------------------------------------------
"""
<아이디어 4 : def를 이용하여 lotto number 추출하기>
"""

def lotto(lottonum):
    print("Your lucky number, {}{}{}{}{}{}".format(lottonum))

### 여기에서 lottomun 이라는 변수의 범위(1~45)를 정의해야할 것 같은데,
# # 1. list 형
# lottonum = [1,2, ..., 45]
# #>> 오류메세지는 없으나 작동이 되지 않음.

# # 2. 범위 잡기
# lottonum = range(1,46)
# #>> 오류메세지는 없으나 작동이 되지 않음.

# 3. lottonum을 정의하고(변수선언?), 범위를 설정해보자
# lottonum =lottonum(range(1,46))
# #>> 오류메세지는 없으나 작동이 되지 않음.

# 4. lottonum의 범위를 그냥 바로 잡아보기
# # lottonum(range(1,46))
# >> 오류발생, lottonum is not defined

# 5. lottonum을 범위를 정하고 해당 범위를 리스트로 잡기
# lottonum = list(range(1,46))
# #>> 오류메세지는 없으나 작동이 되지 않음.

# lottonum = [int(1<45)]
# [1,2, ..., 45]
