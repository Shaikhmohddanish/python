#Dictionary is a {key,value} pairs
dict={"name":"ABC","Rno":43,"Branch":"EXTC"}
print(dict)
#Adding
#key=name,Rno,Branch
#Values=ABC,43,EXTC
dict["course"]="Engineering"
print(dict)
#Modify
dict["course"]="B-tech"
print(dict)
#Deleting
# key word ====> del (one or more elements)
#clear====> clear all the elements (funtions)
del dict["name"]
print(dict)
del dict
print(dict)
