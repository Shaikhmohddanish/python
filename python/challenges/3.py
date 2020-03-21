user=int(input("please enter speed: "))
def speed(n):
    point=0
    if n<=70:
        print("OK")
    elif n>70:
        point=(n//5)-14
        if point >=12:
            print("LICENCE SUSPENDED")
    print(point)
speed(user)