# [예3]: 기회 제한 게임.
# 기억법: 유한반복 조건부반복을 원한다면 while!
# 기억법: 곱집합 식으로 유한반복(요소방문)을 원한다면 for!
# 반복문인데, 반복을 제한하고 싶다는 것. -> 반복에 조건을 걸면됨. (조건부반복)
# 쉽게 말해 반복을 하다가...특정 시기(조건부합 등)에 멈추게 하고 싶다는 것 (무한루프 방지)
# 아래 예문은 사실 무한루프가 아님. 즉 loopbrker를 else에 걸어놓음.
# 다만, 게임횟수를 제한하기 위해 if와 elif에도 brker를 걸어놔야겠음. 이로써 while문 요소가 강조됨!
# while은 조건만족순회...조건만족하는한 영원히 순회. 따라서 1)시작점 2)순회조건 3)명령문 4)순회조건브레이커등
# --> 아래서는 chances=5가 시작점 중 하나? chances -=1가 4), 

import random

answer = random.randint(1, 100)
print(answer)
your_answer = eval(input("Type num."))
chances = 5

while answer != your_answer and chances == 5:
    if answer > your_answer:
        print("Bigger")
        your_answer = eval(input("retype num."))
        chances -= 1
    elif answer < your_answer:
        print("Smaller")
        your_answer = eval(input("retype num."))
        chances -= 1
    else:
        break






''' [예2] 기회 무제한 게임
import random

answer = random.randint(1, 100)
print(answer)
your_answer = eval(input("Type num."))

# 반복문 while: 조건만족순회
# while 조건 만족할 때마다 그 이하 명령문 실행하고 다시 while로 올라옴. 뱅글뱅글.

while answer != your_answer:
    if answer > your_answer:
        print("Bigger")
        your_answer = eval(input("retype num."))
    elif answer < your_answer:
        print("Smaller")
        your_answer = eval(input("retype num."))
    else:
        break
'''

'''
[예1] 이하: SD (코드 중복 너무 많음. 중복(1+1+...+1=100)은 뭐다? 반복문(1x100)으로 축소.)!

import random

answer = random.randint(1, 100)
print(answer)
your_answer = eval(input("Type in a num."))

if answer == your_answer:
    print("True")
elif answer > your_answer:
    print("1/2 to elim. Hint: It's bigger.")
    your_answer2 = eval(input("Type in a num."))
    if answer == your_answer2:
        print("True")
    elif answer > your_answer2:
        print("Wrong. 2/2 to elim. Hint: It's bigger.")
    elif answer < your_answer2:
        print("Wrong. 2/2 to elim. Hint: It's smaller.")
elif answer < your_answer:
    print("1/2 to elim. Hint: It's smaller.")
    your_answer2 = eval(input("Type in a num."))
    if answer == your_answer2:
        print("True")
    elif answer > your_answer2:
        print("Wrong. 2/2 to elim. Hint: It's bigger.")
    elif answer < your_answer2:
        print("Wrong. 2/2 to elim. Hint: It's smaller.")
'''

'''
-> 기회를 얼만큼 줘야? 단판승? Y.
-> 역시 이게 개선점. (Cf. hongsam)
결론: 틀릴 기회5번, 그때마다 힌트(찍은값의 정답대비 대소여부) 제공.

import random

answer = random.randint(1, 100)
print(answer)
your_answer = eval(input("Type in a num."))

if answer == your_answer:
    print("True")
else:
    print("Wrong")


# 입력값 스트링을 정수형변환해주는 방식으로 디버깅함.
# hongsam은 eval메소드씀. 파이썬이 알아서 형태를 유추해서 형변환하는 함수?
