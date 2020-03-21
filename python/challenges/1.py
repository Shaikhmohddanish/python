def speed(v):
    point=0
    if v<70:
        print("OK")
    
    elif 70<v<80:
        point+=1
    elif 80<v<90:
        point+=2
    elif 90<v<100:
        point+=3
    elif 100<v<110:
        point+=4
    elif 110<v<120:
        point+=5
    elif 120<v<130:
        point+=6
    elif 130<v<140:
        point+=7
    elif 140<v<150:
        point+=8
    elif 150<v<160:
        point+=9
    elif 160<v<170:
        point+=10
    elif 170<v<180:
        point+=11
    elif 180<v<190:
        point+=12
    else:
        print("LICENCE SUSPENDED")
        point+=13
    print(point)
speed(179)