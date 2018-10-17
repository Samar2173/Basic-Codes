#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
a=int(input("enter number"))
b=int(input("enter number"))
print("Choice for adding is 1,subtract 2,multiplication 3,division 4")
c=int(input("enter choice"))

if c==1:
 print(a+b)
elif c==2:
 print(a-b)
elif c==3:
 print(a*b)
elif c==4:
 print(a/b)
else:
 print("ERROR") 