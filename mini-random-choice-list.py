#-----------------------------------------------------------------------------
"""
<아이디어 1 : 리스트를 만들고 랜덤으로 프린트하기>
1. import random
2. 랜덤으로 추출할 리스트 만들기 : list_lo =[1,2,3,4,5]
3. 프린트 하기
"""

import random
list_lo = [1,2,3,4,5]
print(random.choice(list_lo))


horses = ["horse1", "horse2", "horse3", "horse4", "horse5"]
secure_random = random.SystemRandom()
print(secure_random.choice(horses))
## list를 만들때,
#horses = ["horse1", "horse2", "horse3", "horse4", "horse5"]
#horses = ["horse1, horse2, horse3, horse4, horse5"]
#은 다른 결과값을 출력한다. "" 한 덩어리를 하나의 문자열로 인식하는 듯 하다.
#-----------------------------------------------------------------------------
"""
<아이디어 2 : 리스트를 만들고 함수를 만들어 특정 영역에 1가지만 랜덤하게 프린트하기>
1. 리스트 만들기
2. {}.format을 사용하여 특정한 문자열이 들어갈 자리 만들기
3. format에 들어갈 내용을 리스트에서 랜덤하게 뽑도록 하기
"""


list_format = ["g","f","e","x","r","l"]
print("{}".format(random.choice(list_format)))

# print(random.choice(list_format))
### print 함수는 int등의 다양한 자료형을 string으로 변환시켜준다.


#-----------------------------------------------------------------------------
"""
<아이디어 3 : randint()함수 사용하기>
## randint() 함수 사용하기
randint(시작범위, 끝범위) ex) randint(1,10) : 1~10까지 랜덤 숫자 생성/range와 다르게 끝 숫자 포함
"""
#randint범위내에서 random하게 추출하기
print(random.randint(1,10))

#randint범위내에서 random하게 여러개추출하기
print(random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45),
    random.randint(1,45))
#-----------------------------------------------------------------------------
"""
<아이디어 4 : def를 이용하여 lotto number 추출하기>
"""
def lotto(lottonum):
    print("Your lucky number, {},{},{},{},{},{}".format(lottonum))

### 여기에서 lottomun 이라는 변수의 범위(1~45)를 정의해야할 것 같은데,
# lottonum = [1,2, ..., 45]
lottonum = list(range(1,46))
# lottonum(range(1,46))  >> 오류발생, lottonum is not defined

# lottonum = [int(1<45)]
# [1,2, ..., 45]


#-----------------------------------------------------------------------------
"""
<add 1. for 를 사용하여 지정한 횟수만큼 숫자 추출하기>
"""
for i in range(1,3): # range(1,n)의 경우 1포함 n-1까지 범위를 설정한다.
    print(random.randint(1,10))

#-----------------------------------------------------------------------------
"""
<search 1. list / len() // if/else를 사용하여 숫자 추출하기>
"""



# from random import randint(str(a))
# print
#여기서 randint 뒤에, 문자가 오게하려면 어떻게 해야할까?


from random import randint
l= ['a','b','c']

def get_rand_element(l):
    if l:
        return l[randint(0,len(l)-1)]
    else:
        return None

print(get_rand_element(l))

#-----------------------------------------------------------------------------


"""
random.sample(range(1,101),1)
random.randint(1,100)
random.choice(range(1,101))
"""
