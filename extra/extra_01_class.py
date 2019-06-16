class Player:
    def __init__(self):
        self.speed = 98

    def getSpeed(self):
        print("speed:%s" % self.speed)  # 우에서 밸류를 받아 좌의 자료형에 넣는?(SD)

    def Shooting(self):
        print("Kabooom!")


cnaldo = Player()
cnaldo.getSpeed()

