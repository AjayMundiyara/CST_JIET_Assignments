a=int(input('Enter value of A : '))
b=int(input('Enter value of B : '))
c=int(input('Enter value of C : '))

sp=0

if(b>c):
 g=b
else:
 g=c

while(True):
 if((g%b==0) and (g%c==0)):
   lcm=g
   break
 g+=1

for i in range(lcm,a+1):
  if(i%lcm==0):
    sp=sp+1

print('Number of special numbers are : ',sp) 