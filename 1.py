a=input()
b=input()
a_10= int(a, 2)
b_10=int(b, 2)
c_10=a_10+b_10
c=bin(c_10)
result=c[2:]
print(result)