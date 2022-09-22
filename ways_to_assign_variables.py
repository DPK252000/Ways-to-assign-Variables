a=1
b=6
c=9
print(a,b,c)
print(a) ; print(b) ; print(c)
print(a)
print(b)
print(c)
print(b,b,c)
print(k)  # NameError: name 'v' is not defined

a=1 ; b=6 ; c=9
print(b)

a,n,e=3,4,6,7 # ValueError: too many values to unpack(expected 3)

a,b,c=4,6 # ValueEroor: not enough values to unpack(expected 3, got 2)

a,b,c,d=2,4,6,8
print(a,b,c,d)

a=c=1 ; b=2 ; d=3
print(a,b,c,d)

print('5th'.isidentifier())
print('phone_k'.isidentifier())
print('_'.isidentifier())

a=3 ; b=6
a,b=b,a
print(a)
print(b)