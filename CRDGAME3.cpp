#  https://www.codechef.com/AUG20B/problems/CRDGAME3

#include <iostream>
#include<bits/stdc++.h>
using namespace std;
void solve(int a,int b)
{
	if(a<10 && b<10)
	{
	cout<<1<<' '<<1<<endl;
	}
	else
	{
	 int c=0;
	 int aaa=0;
	 int c1=0;
	 int aa=a/9;
	 if(a%9!=0)
	 {
	 aa++;
	 }
	 int bb=b/9;
	 if(b%9!=0)
	 {
	 bb++;
	 }
	 if(aa==bb)
	 {
	 cout<<1<<' '<<aa<<endl;
	 }
	 else if(aa>bb)
	 {
	 cout<<1<<' '<<bb<<endl;
	 }
	 else if(aa<bb)
	 {
	 cout<<0<<' '<<aa<<endl;
	 }

	}
}
int main() {
    int t;
    long long int mod=1e9+7;
    cin>>t;
    while(t--)
    {
        int a,b;
        cin>>a>>b;
        solve(a,b);
        
    }
}
