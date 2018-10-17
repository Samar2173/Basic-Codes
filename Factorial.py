#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
n=int(input("enter number"))
j=1
for i in range(0,n):
 if n==0 or n==1:
  print(1)
 else:
  j=(n-i)*j
print(j) 