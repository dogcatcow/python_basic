class MySon:
    def __init__(self, name, age, kind, distinct, speak):
        self.name = name
        self.age = age
        self.kind = kind
        self.distinct = distinct
        self.speak = speak

    def bark(self):
        print(self.speak)


cloud = MySon("구름", "6month", "mix", "very cute", "야옹")
cloud.bark()


# 좌변, 클래스라는 객체생성자(메소드)로 우변 만듦?
# 객체로 메소드호출?
