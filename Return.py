#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module") 
def compute(a):
 print('Num is=',a)
 return a*a,a*a*a
square,cube=compute(4)
print(square,cube)