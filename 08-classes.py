"""
클래스 class
"""
#### ex. Article variables
# title1="개발"
# author1="마르코"
# content1="개발은 쉬워요"
# status1
# view_count1=0
#
# title2="코칭"
# author2="마르코"
# content2="코칭은 쉬워요"
# view_count1=0
#
# title3="창업"
# author3="마르코"
# content3="창업은 쉬워요"
# view_count1=0

### 3개의 변수를 표현한 것


# view_count1=1
# view_count1=2
# view_count1=3
###### 이렇게하면 불편하다

####Article class

# class Article:
#     title="개발"
#     author="마르코"
#     content="개발은 쉬워요"
#     view_count1=0

# class에 있는 내용에 접근하기 위해서
# article1=Article()  # instance를 만들었다. (객체를 만들었다. 클래스의 정보를 가지고 있는 접근가능한 정보를 만들었다.)
# print(article1.title)
#
# article2=Article()
# article2.title="코칭"
# print(article1.title)
# print(article2.title)



#--------------------------------------------------------------------------------------------------------
class Article:
    author="마르코"
    view_count=0
    status="발행중"

    def __init__ (self, title, content): ##__init__ 이라는 함수 : class가 가지고 있는 내장함수, self 등의 변수/ def클래스 안에서 사용되는 함수/ 클래스안에서 만든 함수다 라는 뜻으로 self를 사용
        self.title=title  ## self 의 의미는 클래스 안에 있는 변수들에게 접근하겠다는 약속,
        self.content=content
        self.status

    def read(self): #외부에 read라는 함수를 지정해줌으로써 복잡한 코드를 쉽게 만든다.
        self.view_count=self.view_count + 1


article1=Article("개발","개발은 쉬워요")
article2=Article("코칭","코칭은 쉬워요")
article3=Article("창업","창업은 쉬워요")

print(article1.view_count)
print(article2.view_count)
print(article3.view_count)
#함수를 쓰지 않았다면
#article1.view_count1=article1.view_count1 + 1 : 이렇게 코드를 매줄 짜야한다.
article1.read()
article2.read()
print(article1.view_count)
print(article2.view_count)
print(article3.view_count)
#### 변수의 경우 만드는 만큼인지가 되지만, 클래스의 경우 설정한 영역을 모두 적어줘야한다.

print(article1)
