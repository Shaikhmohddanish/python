even=[2,4,6,8,10]
another_even=even
another_even=list(even)
print(another_even == even)    #== ki jagah is daalo (is purely check karega aur == yahi pe equal hai ye check karega) is wala id se related hai
another_even.sort(reverse=True)
print(even)
a=id(another_even)
print(a)
print(id(even))