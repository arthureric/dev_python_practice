"""
#### for, range(,)
#### while
## '~하는 동안'이라는 뜻이며, 용법이 다르다.
#컴퓨터는 반복을 잘한다.
"""

#### for
for num in range(1,10):  # 1~10이라는 구간이 있는데, 거기서 숫자를 하나씩 꺼내서
    print(num)    # 이 아래에 말하는 대로 처리해줘
# list 중 slice개념 참조; 리스트가 있을 떄, [1,2,3,4,5,][1:3] 마지막 인덱스는 포함하지 않는다.

num_list = [1,2,3,4,5,6,7,8,9]
for num in num_list:
    print(num)

##for loop(for 구문)은 list, tuple, set 등의 목록의 형태로 된것은 모두 받을 수 있다.
##dict의 경우는 쓸 수 있는데 형태가 조금 다르다.


"""
<while>
while True: #무한루프, for 문과 같은 형태로 안에 있는 내용을 반복시켜주는데, while에 있는 조건이 끝날때(false로 바뀔때까지)계속 반복된다.
    print(1) #한 구간이 끝나지 않고 계속 되는 것, command + C 클릭시 끝난다. / control + pause 로 끝내기
    조건이 있다.
"""

a=1
while a<10:
    print(a)
    a=a+1  # =의 경우 왼쪽에다가 오른쪽을 담아줘라 라는 뜻
