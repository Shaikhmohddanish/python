# print(list(range(0,10,2)))
# print(list(range(0,10000,2)))
my_string='abcdefghijklmnopqrstuvwxyz'
print(my_string.index('e'))
print(my_string[4])
danish="danish"
for i in range(0,len(danish)):
    print(danish[i])
small_decimals=range(0,10)
print(small_decimals)
print(small_decimals.index(9))
odd=range(1,10000,2)
print(odd)
print(odd[985])
print(odd.index(985))
sevens=range(7,1000000,7)
x=int(input("Please enter a positive number less than 1M :"))
if x in sevens:
    print(f"{x} is divisible by 7")
else:
    print("NAHI")
