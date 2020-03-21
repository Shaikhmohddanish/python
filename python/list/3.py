even=[2,4,6,8,10]
odd=[1,3,5,7,9]
num=even+odd
num.sort()
print(num)
sorted_number=(sorted(num))
if num==sorted_number:
    print("list equal")
else:
    print("not equal")