print(range(0,5,2)==range(0,6,2))
print(list(range(0,5,2)))
print(list(range(0,6,2)))
r=range(0,100)
print(r)
print('='*50)

for i in r[::-2]:
    print(i)
print('='*50)

for i in range(99,0,-2):

    print(i)
print('='*50)
print(range(0,100)[::-2]==range(99,0,-2))
for i in range(0,100,-2):                      #no output 

    print(i)
for i in range(100,0,-2):
    print(i)