def idMaker(a):
    b = a[6+1]
    if b == "1" or b == "3":
        print("Male")
    elif b == "2" or b == "4":
        print("Female")


hito1 = "950815-1846739"
hito2 = "990829-3846739"
hito3 = "910210-2846739"
hito4 = "960829-4846739"

idMaker(hito1)
idMaker(hito2)
idMaker(hito3)
idMaker(hito4)
