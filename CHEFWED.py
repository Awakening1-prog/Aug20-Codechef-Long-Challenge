#  https://www.codechef.com/AUG20B/problems/CHEFWED


# cook your dish here
from collections import Counter
t1=int(input())
mod=1000000007
for i in range(t1):
    m1,k1=map(int,input().split())
    a1=list(int(x) for x in input().split())
    h1={}
    res1=[]
    m1=[]
    res11=[]
    res111=0
    c1=0
    for i in a1:
        if i not in h1:
            h1[i]=1
        else:
            h1[i]+=1
    for key,val in h1.items():
        if val>1:
            res111+=val
    s_min1=(k1+res111)
    for i in range(len(a1)):
        if a1[i] not in res1:
            res1.append(a1[i])
        else:
            res11.append(res1)
            res1=[]
            res1.append(a1[i])
    res11.append(res1)
    x1=k1*len(res11)
    a1.sort()
    for i in range(len(a1)-1):
        if a1[i]==a1[i+1]:
            c1+=1
        else:
            if c1!=0:
                m1.append(c1+1)
            c1=0
    if c1!=0:
        m1.append(c1+1)
    print(min(x1,sum(m1)+k1,s_min1))