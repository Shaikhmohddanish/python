menu=[]
menu.append(['egg','spam','beacon'])
menu.append(['egg','saus','beacon'])
menu.append(['egg','spam'])
menu.append(['egg','beacon','spam'])
menu.append(['egg','beacon','saus'])
menu.append(['egg','beacon','saus','spam'])
menu.append(['spam','beacon','saus','spam'])
menu.append(['spam','egg','spam','beacon','spam'])
menu.append(['spam','egg','saus','spam'])
menu.append(['spam','spam','beacon','egg','spam','saus','beacon'])
for meal in menu:
    if 'spam' not in meal:
        print(meal)
        meal.append("spam")
        print(meal)
        for value in meal:
            print(value)