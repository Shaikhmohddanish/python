li=[1,2,3,4,5,6,7,8,9,10]
my_iterator=iter(li)
for i in range(len(li)):
    print(next(my_iterator))
list=["monday",'tuesday','wednesday','thursday','friday','saturday','sunday']
my_iterator1=iter(list)
for i in range(len(list)):
    print(next(my_iterator1))