#### boolean : 참과 거짓
#### if : 이것을 이용하여 컴퓨터에게 판단을 할 수 있도록 권한을 컴퓨터에 위임
# 사람 vs 컴퓨터 : 사람은 스스로 판단할 수 있는데, 컴퓨터는 사람이 알려줘야한다.



#### if
### True
### False 로 인지하는 경우
# constants defined to be false : None / False
# zero of any numeric type(0과 관련된 숫자타입) : 0, 0.0, oj. / Decimal(0) / Fraction(0,1)
# empty sequences and collections (비어있는 경우) : '',(), [], {}, set(), range()


#### boolean Operations - and, or, not 참, 거짓

a = True
b = False
# A 가 참이다. 그리고 B가 참이라면 (A와 B 둘다 참이어야 된다.)
print(a and b) # 결과값 : False

# A 가 참이거나 혹은 B가 참이라면 (A나 B 둘중에 하나라도 참이면 된다.)
print(a or b) # 결과값 : True

print(a==True)
print(a is True)


# if x is false, then True / else False
print(not a) # 결과값 : False
print(not b) # 결과값 : True
print(not a == b) # 결과값 : True
print(not (a == b)) # 결과값 : True
# print(a == not b)  >> syntax error



#### Comparisons

"""
<	strictly less than
<=	less than or equal
>	strictly greater than
>=	greater than or equal
==	equal
!=	not equal
is	object identity
is not	negated object identity
= 값을 할당, 대입
"""



#### if
d=7
if d>10:   # if에 속하는 부분은 tab으로 한번 띄워줘야한다.
    print("숫자는 10보다 큽니다.")
# 구간을 나누고 싶으면 elif
elif d > 5 and d <= 10:
    print ("숫자는 10보나 작거나 같고, 5보다는 큽니다.")

else :
    print("숫자는 5보다 작거나 같습니다.")
