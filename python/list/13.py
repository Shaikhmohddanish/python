# small_decimal=range(0,10)
# print(small_decimal)
# my_range=small_decimal[::2]
# print(my_range)
# print(my_range.index(4))
deciam=range(0,100)
my_range=deciam[3:40:3]
for i in my_range:
    print(i)
print('='*50)
for i in range(3,40,3):
    print(i)
print(my_range==range(  3,40,3))