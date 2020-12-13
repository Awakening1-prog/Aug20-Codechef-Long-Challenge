#   https://www.codechef.com/AUG20B/problems/SKMP

# cook your dish here
def solve(a1,b1):
    a1=sorted(a1)
    a1=''.join(a1)
    if b1[0] in a1:
        x1=a1.index(b1[0])
        y1=a1.rindex(b1[0])
    else:
        m1=0
        for i in range(len(a1)):
            if a1[i]>b1[0]:
                m1=i
                break

        x1=m1
        y1=m1
    if (y1+2)<len(a1):
        y1=y1+2
    else:
        y1=len(a1)
    res11=''
    l=[]
    for i in a1:
        res11+=i
    for i in range(x1,y1+2):
        res11=res11[:i]+b1+res11[i:]
        l.append(res11)
        res11=a1
    #print(l)
    print(min(l))


t2=int(input())
for i in range(t2):
    aa=input()
    bb=input()
    h={}
    for i in aa:
        if i not in h:
            h[i]=1
        else:
            h[i]+=1
    res1=''
    h1={}
    for i in bb:
        if i not in h1:
            h1[i]=1
        else:
            h1[i]+=1
    for key,val in h1.items():
        if key in h:
             h[key]-=val
    for key,val in h.items():
        res1+=key*val
    #print(res)
    if res1==bb:
        print(aa)
    else:
        solve(res1,bb)