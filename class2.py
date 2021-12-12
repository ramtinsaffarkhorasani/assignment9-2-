a=int(input("enter hour(first time)"))
b=int(input("enter minaute(first time)"))
c=int(input("enter second(first time)"))
d=int(input("enter hour(second time)"))
e=int(input("enter minaute(second time)"))
f=int(input("enter second(second time)"))
h=input("what do you want i do + or -")
class timee:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
t1=timee(a,b,c)
t2=timee(d,e,f)
if h == "+":
    a2=t1.h+t2.h
    b2=t1.m+t2.m
    c2=t1.s+t2.s
if h == "-":
        a2=t1.h-t2.h
        b2=t1.m-t2.m
        c2=t1.s-t2.s
print("the answer is",a2,":",b2,":",c2,)    
