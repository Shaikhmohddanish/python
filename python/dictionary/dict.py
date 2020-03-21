# DICT={expression iteration condition(optional)}     dictionary creation
#CREATION
dict={x:x**2 for x in range(5) if x%2==0}
print(dict)
danish={x:x**2 for x in range(11) if x%2==0}
print(danish)
harish={x:x**2 for x in range(11)}
print(harish)




#ACCESSING


#with the help of keys we can access corresponding values

dict1={"name":"ABC","dect":"extc","rno":43}
a=dict1["name"]
b=dict1["dect"]
c=dict1["rno"]
print(a,b,c)
hey=dict1.items()
print(hey)