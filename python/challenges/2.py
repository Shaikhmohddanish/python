user=int(input("Speed De apun uski maarta hai BTC :"))

def speed(n):
    point=0
    if n<=70:
        print("OK")
    elif n>70:
        for i in range(0,((n-70)//10)*2):
            point+=1
        if point>=12:
            print("LICENCE SUSPENDED")
    if user%5==0 and user%10!=0:
        point+=1
    for i in range(6,10):
        if user%10==i:
            point+=1
    print(point)
speed(user)