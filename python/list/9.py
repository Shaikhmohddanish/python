#Iterators
string="1234567890"
# for char in string:
#     print(char)
my_itrator=iter(string)
# print(my_itrator)
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))
# print(next(my_itrator))

for char in string:
    print(char)
for char in iter(string):
    print(char)
