string="1234567890"
# for i in string:
#     print(i)
my_iterator=iter(string)
print(my_iterator)
for i in range(1,11):
    print(next(my_iterator))
# for i in my_iterator:
#     print(next(i))