# Quiz 04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)
# SD: 문풀 중 특이사항 cf로 북마크.

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print("apple;orange;banana;lemon")
print("hello")
# 3. 화면에 * 기호 100개를 표시하세요.

print("*" * 100)
# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

print(type((int("30"))))

'''
# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
strex = "Niceman"
print(strex[4:6+1])    # why 6+1? 레인지같은것.rc.구구단...cf  슬라이싱?
'''
'''
# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
strex2 = "Strawberry"
print(reversed(strex2))  # 이상한 값 나옴...cf
'''

'''
# 따로 검색해서 코드 재작성:
print("Strawberry"[::-1])  # cf. 전에 인코더 만들때, 요소순회방문 순서 거꾸로했던 것.

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
# cf. 따로 검색해서 코드 재작성:

num = "010-7777-9999"
print(num.replace('-', ''))

print(ord('-'))
print(num.translate({ord('-'): None}))  # Cf. dict 모양? {키:밸류?}

'''

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
strex = "http://daum.net"
print(strex[7:15+1])

'''
# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
# cf. 별도 검색, 코드 작성:


strex = "NiceMan"
print(strex.lower())
print(strex.upper())
'''

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
strex = "abcdefghijklmn"
print(strex[2:4+1])

'''
# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
# cf. 별도 검색, 코드 작성: 이게 최선? 인덱스값으론 못 뺌?
a = ["Banana", "Apple", "Orange"]

a.remove("Apple")  # 비효율적...값을 알아야되니까.
print(a)

b = ["Barney", "Batman", "Banquo"]
del b[1]
print(b)
'''

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tuplex = (1, 2, 3, 4)
print(type(list(tuplex)))


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
feebox = {"성인": "100000", "청소년": "70000", "아동": "30000"}
print(type(feebox))

'''
# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
# cf. 별도 검색, 코드 작성
feebox['소아'] = '0'
print(feebox)
'''

'''
# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
# cf. 별도 검색, 코드 작성
print(feebox.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(feebox.values())

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
'''
