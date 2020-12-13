#  https://www.codechef.com/AUG20B/problems/LINCHESS


# cook your dish here
import operator
t1=int(input())
for i in range(t1):
    m,k=map(int,input().split())
    arr=list(int(x) for x in input().split())
    h={}
    for i in range(len(arr)):
        if k%arr[i]==0:
            h[arr[i]]=k//arr[i]
    h1=dict(sorted(h.items(),key=operator.itemgetter(1)))
    if len(h1)==0:
        print(-1)
    else:
        l1=[]
        for key in h1.keys():
            l1.append(key)
        print(l1[0])