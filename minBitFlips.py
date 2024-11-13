from math import log2

class Solution(object):
    def minBitFlips(start, goal):
        mods=[]
        mods1=[]
        cont=0
        a1=[]
        a2=[]
        if goal==0 and start==0:
            flips=0
        elif goal==start:
            flips=0
        elif goal==0 and start!=0:
                for i in range(0,int(log2(start))+1):
                        x=start/2
                        y=0*i
                        mod1= start%2
                        mod2=y
                        start=int(x)
                        mods.append(mod1)
                        mods1.append(mod2) 
                        p=mods[i]
                        q=mods1[i]
                        if p!=q:
                            cont+=1
                        flips=cont
                        a1.append(p)
                        a2.append(q) 
        elif start==0 and goal!=0:
                for j in range(0,int(log2(goal))+1):
                        x=0*j
                        y=goal/2
                        mod1= x
                        mod2=goal%2
                        goal=int(y)
                        mods.append(mod1)
                        mods1.append(mod2) 
                        p=mods[j]
                        q=mods1[j]
                        if p!=q:
                            cont+=1
                        flips=cont
                        a1.append(p)
                        a2.append(q)
        else:
            m=int(log2(goal))
            n=int(log2(start))
            if start<goal:
                    for i in range(0,m+1):
                        x=start/2
                        y=goal/2
                        mod1= start%2
                        mod2= goal%2  
                        start=int(x)
                        goal=int(y)
                        mods.append(mod1)
                        mods1.append(mod2)     
                    for j in range(m+1):
                        p=mods[j]
                        q=mods1[j]
                        if p!=q:
                            cont+=1
                        flips=cont
                        a1.append(p)
                        a2.append(q)
            elif start>goal:
                    for i in range(0,n+1):
                        x=start/2
                        y=goal/2
                        mod1= start%2
                        mod2= goal%2  
                        start=int(x)
                        goal=int(y)
                        mods.append(mod1)
                        mods1.append(mod2) 
                    for k in range(n+1):
                        p=mods[k]
                        q=mods1[k]
                        if p!=q:
                            cont+=1
                        flips=cont
                        a1.append(p)
                        a2.append(q)
        return (flips)

start=int(input("start: "))
goal=int(input("goal :"))
flips=Solution.minBitFlips(start,goal)
print(flips)