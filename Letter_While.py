#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
a=input('Enter String')
if len(a)%2==0:
 print(a.capitalize()) 
else:
 for i in a:
  a=i+a
 print(a) 