#OCTAL
powers=[]
for power in range(15,-1,-1):
    powers.append(8**power)
# print(power)
x=int(input("PLEASE ENTER A NUMBER: "))
printing=False
for power in powers:
    bit=x//power
    if bit !=0 or power==1:
        printing=True
    if printing:
        print(bit,end="")
    x%=power
