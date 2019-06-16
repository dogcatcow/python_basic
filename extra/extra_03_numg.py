# FC_CS PY 13강
# numguess (if문 관련)

# 문제 분해 (단계 세팅) - Hongsam

'''
1. 컴터가 난수를 생성한다. (1~100 사이.)
-> rand 이용? 메소드?
2. 사용자로부터 숫자를 입력받는다.
3. 입력받은 숫자가 난수와 같은지 비교한다/
4. 같으면 정답, 틀리면 오답.
-> 기회를 얼만큼 줘야? 단판승?

'''
'''
import random

answer = random.randint(1, 100)
print(answer)

val = int(input("Enter your value: "))

if val == answer:
    print("True")
else:
    print("False") 
# by SD
'''


answer = random.randint(1, 100)
print(answer)
your_answer = input("Type in a num.")

if answer == your_answer:
    print("True")
else:
    print("Wrong")
