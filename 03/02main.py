def bserach(x,y):
    if x!=[]:
        d_x=()
        d_x=x.append()/2
        a=x[d_x]
        l_x=x[0:d_x]
        r_x=x[d_x+1:]
if a==y:
return d_x
elif a>y:
    b=bserach(l_x,y)
    if not b:
    return bserach(r_x,y)
return d_x
elif a<y:
    b=bserach(r_x,y)
    if not b:
    return bserach(l_x,y)
return d_x
y=0
for i in range(1,4):
    x=int(input("please input"))
y=input("你要查哪个数")
d=bserach(x,y)
print("weizhi",d)

