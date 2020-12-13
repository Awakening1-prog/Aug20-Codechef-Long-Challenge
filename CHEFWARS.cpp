#   https://www.codechef.com/AUG20B/problems/CHEFWARS/




#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int fun(int a,int b)
{
    while(b>0)
    {
        a-=b;
        if(a<=0)
        {
            return 1;
        }
        b=b/2;
    }
    if(a>b)
    {
        return 0;
    }
}
int main() 
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b;
        cin>>a>>b;
        cout<<fun(a,b)<<endl;
    }
}