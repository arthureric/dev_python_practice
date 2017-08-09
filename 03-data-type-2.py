#### 목록 list, tuple
#### 사전 dict - dictionary
#### 집합 set


#### list []
print([1,2,3])
print(type([1,2,3]))

list_a = [1,2,3]
print(list_a)
print(list_a[1])
# index (몇번째?) 는 0부터 시작한다. 첫번째를 뽑아내려고 한다면 0에 해당하는 위치를 넣어햐 한다.
print(list_a[0])
print(list_a[1])
print(list_a[2])

# slice : 리스트를 자른다. 시작하는 인덱스와 마지막 인덱스를 넣어주고, 마지막 인덱스는 제외한 채로 선택된다.
print(list_a[1:3])
print(list_a[0:2])
print(list_a[2:3])

# append :추가하는 것
list_a.append(4)
print(list_a)

list_a.append(7)
print(list_a)

# remove : 제거하는 것, 지칭하는 것은 목록의 순서가 아니라 해당 값을 의미한다.
list_a.remove(2)
print(list_a)


list_a.clear()
print(list_a)
# clear :


#### tuple (1, ) - 최소한 값 하나와 쉼표를 넣어줘야 튜플로 인식한다.
# tuple 은 list와 다르게 다른 항목을 추가하거나 없애거나 할 수 없다.
# 한번 생성 후 내부 값 변경 불가
print("tuple")
print((1,2,3))
print(type((1,2,3)))

tuple_a = (1,2,3)
print(tuple_a)
print(type(tuple_a))
# tuple_a.append(4)  >> 이렇게 하면 오류가 발생한다, tuple은 list와 다르게 추가적으로 내부값을 변경할 수 없다.



#### 변경 가능한 list가 있는데, 굳이 tuple을 만드는 이유는?  1. 폐쇄적 안정성, 2. 속도 올리기
# list는 다양한 기능을 가지고 있다 > programming 관점에서 봤을때, 많은 자원을 사용하고 있다.
# 변경가능성이 없는 경우는 tuple을 사용하여 속도를 높이는데 기여한다.
# 프로그래머가 의도적으로 이부분은 바뀌면 안돼! 라고 안정성을 기하고 싶은 경우 tuple을 사용한다.



#### dict - dictionary  (map)  :  {}
# key & value 값을 가지고 있다.
# dict = {"key" : "value"}
dict_a = {
    "apple" : "a type of fruit",
    "pen" : "a thing to write"
    }
print((dict_a))
print(dict_a["apple"])

# edit value
dict_a["pen"] = "something to write"
print(dict_a)
# dict의 경우, 변경하고 싶을 때, 추가적으로 설정할 수 있다.




####set  set([]) : 집합이라고 생각하면 된다. 잘 안사용되어서 본인의 모양도 없다.
set_a = set([1,2,3])
set_b = set([2,4,6])
print(set_a)
print(set_b)

### 중복제거!
### 교집합, 합집합, 차집합, 여집합
# 중복이 없다./자동으로 중복 제거
# ex. list의 경우 1,2,3,3,4 가 가능하지만, set의 경우는 1,2,3,4 처럼 중복이 불가능하다.

# 교집합 : &
print(set_a & set_b)

#합집합 : |
print(set_a | set_b)

# 차집합 : -
print(set_a - set_b)
