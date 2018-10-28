amt, denom = input().split()
amt=int(amt)
denom=int(denom)

coin = [int(x) for x in input().split()]
change=[]

for i in range(0, amt+1):
    change.append(0)

for i in range(1, amt+1):
    mincoins=999999
    for j in range(0, len(coin)):
        if(i>=coin[j]):
            mincoins=min(mincoins, change[i-coin[j]]+1)
    change[i]= mincoins
print(change[amt])                    
