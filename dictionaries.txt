#Methods
#(key,value)=====>tuple
#1. Copy()====> copy the key-value pairs into another variable. Syntax- dict.copy()
a={"NAme":"DAnish","roll":43,"Class":2,"course":"btech"}
b=a.copy()
print(b)
#2. clear()====> remove all the key-value pairs. Syntax- dict.clear()=====>empty dictionary { }
# a.clear()
# print(a)
#3. items()====> display all the key-value pairs available in dictionary in the form of tuple. Syntax- d.items()
i=a.items()
print(i)
#4. keys()=====> display all the keys in dictionary. Syntax- d.keys()
k=a.keys()
print(k)
#5. values()=====> display all the values in dictionary. Syntax- d.values()
v=a.values()
print(v)
#6. update()=====> Add one or more items into existing dictionary. Syntax- d.update({"branch":"extc","place":"panvel"})
u=a.update({"branch":"extc","place":"panvel"})
print(a)
#7. pop()=====> Delete an item from dictionary Return the value of a key which is removed. Syntax- d.pop(key,value(optional))
p=a.pop("course")
print(a)
print(p)
p1=a.pop("place","panvel")
print(p1)
#8 get()=====> one  argument(key) display the value of given key. Syntax- d.get(key) ex- d.get("roll")=====>43
g=a.get("roll")
print(g)
#9 fromkeys()========> it takes 2 arguments 1.tuple or sequence(keys)  2.value(for all keys). Syntax- exapmle t=("a","b","c")   v=0
# d.fromkeys(t,0)=====>{"a":0,"b":0,"c":0}
f=a.fromkeys("NAme","DAnish")
print(f)
#10 setdefault()=======> It takes two arguments 1.key and 2.value Syntax- d.setdefault(key,value)
#example   d.setdefault("branch","extc")
s=a.setdefault("branch","mech")
print(s)                            #q ki branch exists tha pehle se isliye no changes
s1=a.setdefault("pec",90)
print(s1)
print(a)
#11 popitem()=====>it deletes recently inserted item only 1 item(key+values)
a.popitem()
print(a)