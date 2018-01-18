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



#### Article class inheritance 상속
"""
class BrunchArticle:
       author="마르코"
        view_count=0
        source = "브런치" # Brunch에서만 가지고 온 소스이기 때문에

        def __init__ (self, title, content): ##__init__ 이라는 함수 : class가 가지고 있는 내장함수, self 등의 변수/ def클래스 안에서 사용되는 함수/ 클래스안에서 만든 함수다 라는 뜻으로 self를 사용
            self.title=title  ## self 의 의미는 클래스 안에 있는 변수들에게 접근하겠다는 약속,
            self.content=content
            self.status

        def read(self): #외부에 read라는 함수를 지정해줌으로써 복잡한 코드를 쉽게 만든다.
            self.view_count=self.view_count + 1
해당 내용을 하기 사항으로 대체 가능
"""
class BrunchArticle(Article):
    source="브런치"

    def read(self): #부모 클래스에서 가지고 있던 함수를 자식 클래스에서 덮어쓸수 있다.
        self.view_count=self.view_count + 2 #override 했다라고 표현 / 자식 클래스가 다시 오버라이드 했을때, 자식 클래스 내에서 덮어쓴 함수를 사용


brunch_article=BrunchArticle("개발", "개발은 쉬워요")  #브런치 아티클 활성화 _ 인스턴스 만든다고 표현
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
#함수 또한 가지고 올 수 있다. 부모클래스의 함수를 가지고 온 것을 확인할 수 있다.
