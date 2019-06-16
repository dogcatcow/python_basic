# Quiz05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)
# 푸는법: 해결 절차는 아는데 정확한 툴이름이 기억안나면 일단 절차설명cf.->툴검색->적용

'''
# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
# cf. 딕셔너리에서 3번째 키의 값을 가져오기:

q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
# cf. 딕셔너리에서 3번째 키의 값을 가져오기:

q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
'''

'''
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = int(input("Type score:"))
if score >= 81 and score <= 100:
    22
    print("A학점")
elif score >= 61 and score <= 80:
    print("B학점")
elif score >= 41 and score <= 60:
    print("C학점")
elif score >= 21 and score <= 40:
    print("D학점")
elif score >= 0 and score <= 20:
    print("E학점")
'''
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
'''
# Rc. cartesian prod, non-reflex, had 3 ordered pairs,
# ab bc ca. all examined.

no = [12, 6, 18]

if no[0] > no[1]:  # a>b
    if no[0] > no[2]:  # a>b &&(indent.) a>c
        print("{} is the max.".format(no[0]))  # max: a
        # compared: a-b, a-c
    elif no[2] > no[0]:  # a>b && c>a
        print("{} is the max.".format(no[2]))  # max: c
        # compared: a-b, c-a
elif no[0] < no[1]:  # a<b
    if no[1] > no[2]:  # b>a && b>c
        print("{} is the max.".format(no[1]))  # max: b
        # compared: a-b, b-c
'''

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
# cf. 1) split으로 2개로 만든다
# 2) 리스트에 담겨진 두개 스트링 중 후자를 인덱싱해서 변수에 담기
# if 변수가 1or3 이면 남.

# Can I use less codes?
# if you have many values in field -> use class?
# if와 elif에 return 안붙여도됨.
# 에러시: ctrlshfitb  / 우클릭 run in terminal / 상단메뉴 run w/o debug?
'''
def idMaker(a):
    b = a[6+1]
    if b == "1" or b == "3":
        print("Male")
    elif b == "2" or b == "4":
        print("Female")    
    
hito1="950815-1846739"
hito2="990829-3846739"
hito3="910210-2846739"
hito4="960829-4846739"
    
idMaker(hito1)
idMaker(hito2)
idMaker(hito3)
idMaker(hito4)
'''

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
'''
q3 = ["갑", "을", "병", "정"]
# cf. 빼고 프린트하라? 몰라서 그걸 뺀 ~~만 출력하라로 일단 했음.

print(q3[0:2], q3[3])
'''

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
#cf. 선택자! Cf. HTML-CSS. 여기서는 홀수!!선택자!!를 몰라서 진행불가?
#마찬가지로, 인덱싱도 결국은 선택자 관련.
#클래스와 메소드호출 등도 결국 선택자 관련?

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
#cf. 선택자! Cf. HTML-CSS. 여기서는 홀수!!선택자!!를 몰라서 진행불가?


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
#cf. 선택자! Cf. HTML-CSS. 여기서는 홀수!!선택자!!를 몰라서 진행불가?


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
#cf. 선택자! Cf. HTML-CSS. 여기서는 홀수!!선택자!!를 몰라서 진행불가?
#cf. HTML-CSS의 uppecase 스타일링?
'''
이상 결론: ~는 다른언어의 ~의 해당한다고 느낄 때가 많음.
결국 프로그래밍은 요소선택과 제어라서?
'''