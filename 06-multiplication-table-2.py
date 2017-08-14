
number = input("몇 단을 출력하시겠습니까?")
print(number, "단")
number = int(number)

for b in range(1, 10):

    # print(number, "*", b, "=",  number * b)
    print("{} * {} = {}".format(number,b,number*b))
