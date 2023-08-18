x = int(input('삼각형의 한 변 x의 길이 입력:'))
y = int(input('삼각형의 한 변 y의 길이 입력:'))
z = int(input('삼각형의 한 변 z의 길이 입력:'))
if x < y+z and y < x+z and z < x+y:
    print('삼각형을 구성할 수 있음')
else:
    print('삼각형을 구성할 수 없음')