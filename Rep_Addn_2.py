#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")

x=int(input('Enter Upper Number')) 
y=int(input('Enter Lower Number')) 
z=0
if y>x:
 print('Invalid Input') 
elif x!=0 and y!=0:
 for i in range(y,x+1):
  z+=i
 print(z)
else:
 print('BYE BYE') 