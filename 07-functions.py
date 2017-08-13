"""
함수 - functions
입력값 parameters, 반환값 return
"""
"""
함수는 def(definition의 약자) 로 생성, 중복되는 부분을 단순하게 만들어준다.
향후 수정할 이유가 생겼을 때 단순히 함수안에 있는 내용만 고치면 된다.
"""

def hello_friends(name):
    print("hello, {}".format(name))
#name : parameters, return은 없는 형태이다.

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "peter"
name6 = "janstine"
name7 = "johnwick"
name8 = "tomboy"


# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))
# print("hello, {}".format(name5))
# print("hello, {}".format(name6))
# print("hello, {}".format(name7))
# print("hello, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)



"""
함수 구성요소 :입력값 parameters, 반환값 return
parameters가 있다/없다
return값이 있다/없다
4종류
"""
# 1. parameters O , return O
def sum(a,b):
    return a + b

# 2. parameters O , return X
def hello_friends(name):
    print("hello, {}".format(name))

# 3. parameters X , return O
def return_1() :
    return 1

# 4. parameters X , return X
def hellot_world():
    print("hello world")

"""
return은 변수에 담아서 쓸 수 있다.
"""

num_1 = return_1()
print(num_1)
