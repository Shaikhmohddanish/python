user_name=input("Please enter your username :")
password=input("please enter password that contain atlease\nSmall Alphabet,Capital Alphabet,a number and special character \nAnd password length should be in 6 to 12 :")
small=[]
capital=[]
numbers=[]
special=[]
for i in range(97,123):
    small.append(chr(i))
for i in range(65,91):
    capital.append(chr(i))
for i in range(0,10):
    numbers.append(i)
for i in range(33,65):
    special.append(chr(i))
print(len(special))
for i in range(0,len(password)):
    if len(password)<6:
        print("Please Enter password which has length 6 to 12 :")
        password=input()
    elif 6<=len(password)<=12:
        for j in range(0,26):
            if password not in small:
                break 
