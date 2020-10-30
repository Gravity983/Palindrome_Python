prime=[]
count=0
ll=int(input())
hl=int(input())
for num in range(ll,hl+1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
print (prime)
 for x in range (0,len(prime)):
  for i in range (0,len(prime)):
    if (prime[x]-prime[i]==6):
      print(prime[i],"and",prime[x],"is a sexy pair")
      count+=1
print("in total",count,"sexy pairs")
