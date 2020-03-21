menu=[]
menu.append(['a','b','c'])
menu.append(['a','d','e','f'])
menu.append(['a','d','e','f','g'])
menu.append(['a','h','e','y'])
menu.append(['h','i','j'])
for value in menu:
    if 'a' not in value:
        print(value)