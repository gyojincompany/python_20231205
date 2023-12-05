list1 = [1,2,3] # iterable 반복 가능 객체

for i in list1:
    print(i)

# print(next(list1)) # 에러발생->리스트는 iterable객체지만 iterator는 아니다

iter1 = iter(list1) #iterator 선언

print(type(iter1))

print(next(iter1))
print(next(iter1))
print(next(iter1))

a = 10

a = 10.5

a = "korea"

# int a = 10; java의 경우 변수선언 시 자료타입을 맨 앞에 선언해야 함
# a = 10.5

b: int = 10 # 정수형으로 힌트만 줄뿐 정수형 변수로 고정시키는 것이 아님
b = 10.5

def sum(a: int, b: int) -> int:
    return a+b

result = sum(10, 20.5)

