#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll arr[100001];
  int main()
{
    ll a,b,c,d,e,f,g,h,i;
    memset(arr,0,sizeof(arr));arr[0]=arr[1]=0;

    for(b=2;b<=100000;b++)
    {
        for(c=2;c<=sqrt(b);c++)
        {
            d=b;
          while(d%c==0)
          {//cout<<d<<" "<<c<<"\n";
          d=d/c;
              arr[b]++;
          }
        }
        if(d>1)arr[b]++;
    }

    cin>>a;
    for(b=0;b<a;b++)
    {
        cin>>c>>d;f=0;
        for(e=c;e<=d;e++)
        {
            if(arr[e]>=4){f++;}
        }
        cout<<f<<"\n";
    }
}