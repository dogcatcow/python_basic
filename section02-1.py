# section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본 출력

# print('yo')
#print("yo wussup")
#print("""hello py""")
#print('''hello py''')

# 파이썬 자료형 링크:

"""[V1]-------------------------------------------
print()  # 이 자체로만으로는 줄 바꿈임.

# Seperator 옵션:

print('T', 'E', 'S', 'T', sep='')  # '무칸'으로 분리해놓음.


print('T', 'E', 'S', 'T', sep='/')  # '/' 칸으로 분리.

print('2019', '02', '11', sep='/')

print('mitch00bot', 'gmail.com', sep='@')


# end 옵션 사용

print("Why she had to go I don't know...", end=' ')  # 줄바꿈없이 다음 줄 연결.
print("she wouldn't say...", end=' ')  # 단, 여기선 공백 ' '으로 연결됨.
print("blah blah yesterday.")  # end가 없으니 이후는 줄바꿈. rc. print()는 줄바꿈.
print("-BTS")

"""
"""
[V2]-------------------------------------------
# 참조 : https://www.python-course.eu/python3_formatted_output.php
# format 사용 [] {} ()
# 정확도 순서 [0]<[1]<[2]
"""

"""
print('{} and {}'.format('You', 'Me')) #[0]
print('{0} and {1} and {2}'.format('A', 'B', 'C'))
print('{} and {} and {}'.format('A', 'B', 'C'))
print('{a} and {b}'.format(a='You', b='Me'))  #[1] 아래 예시의 컴프리헨션. 함수안에서 변수선언 한 셈.
a = 'You'
b = "Me"
print('{} and {}'.format(a, b))

print("%s's favorite number is %d" % ('SD', 0))  #[2] %s: 문자 %d:정수 %f: 실수
"""


# [V3]-------------------------------------------

print("Test1: %5d, Price: %10.2f" %
      (4, 65.724565141221))   # %(d=724565,f) 동시선언 느낌?
# 즉, %5d는 d를 위해 _ _ _ _ _ 자료형 그릇에 5개 슬롯 주겠다?
# 5자리슬롯인데, 1자리만 프린트하라고 했을때 from(*1) 빈칸 보면 답나옴. 위: 각각 (5-1)자리, (10-2)자리.

print("Test1: {0:5d}, Price: {1:4.2f}".format(776, 6534.123))
# 0,1,2,3...키값. 5d, 4.2f...밸류? 아니면 키값의 연장?
# 그러고보니..형식이 딕셔너리와 비슷? {key : value} ...?   ~format 메소드는 필드값을 넘겨받음?

# a,b는 0,1처럼 내장X? 변수선언해줘야? Cf.위: 컴프리헨션.
print("Test1: {a:5d}, Price: {b:4.2f}".format(a=776, b=6534.123))


"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자   #여기까지만 알아도.
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...
"""


print("'you'")
# print('''') 1)의도:''출력 2)문제: 동시 처리해야할 건이 2건 '',''이 되어버림.
# 해결(아래):

print('\'\'')  # \' 역슬러시에 태워, 도망시킴. 이스케이프.

print('\\you\\')

print('\\you\\\n')  # 줄바꿈된거..cmd의 빈칸에서 확인. 빈칸rtd. to[*1]
# print('\->\  you  \->\   \n=개행(라인브레이킹) )

print('\\you\\\nlinebroke')

print('\\you\\\n\t\t\tlinebroke')
