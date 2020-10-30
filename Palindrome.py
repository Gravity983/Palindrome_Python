pal=[]
st=int(input("enter starting range:"))
so=int(input("enter stop value:"))
off=int(input("enter offset value:"))
for x in range(st,so):
  sum=0
  ori=x
  while(x!=0):
    d=x%10
    sum=sum*10+d
    x=x//10
  if (sum==ori):
    pal.append(ori)
print(pal)
if(pal[len(pal)-1]-pal[0]<off):
  print(len(pal)-1)
else:
  print(len(pal))
