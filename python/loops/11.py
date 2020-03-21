from functools import reduce
li=[1,2,3,4,5,6,7,8,9,10]
Danish=(reduce(lambda a,b:a+b,li))
print(Danish)