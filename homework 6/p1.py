l1=[2,3,4,5,6,7,8,9,10]
evenlist=[]
oddlist=[]
even=0
odd=0
for l1 in l1:
   if l1%2==0:
      even=even+1
      evenlist.append(l1)
   else:
      odd=odd+1
      oddlist.append(l1)
print(f"there are {even} even number and they are {evenlist}")
print(f"there are {odd} odd number and they are {oddlist}")
        
   
    