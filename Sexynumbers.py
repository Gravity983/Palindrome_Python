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
//What to do further
print("in total",count,"sexy pairs")