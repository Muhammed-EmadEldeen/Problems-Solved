#include<iostream>
#define ll long long
ll mii =1;
using namespace std;

int main(){
    ll t;
    cin>>t;
    while(t--){
        ll n,q;
        cin>>n>>q;

        ll bigger_before[n];
        ll bigger_after[n];

        ll max=0;
        ll id_max=0;
        
        for (ll i=0;i<n;i++){
            ll num;
            cin>>num;
            if (num>max){
                bigger_before[i]=i;
                bigger_after[i]=0;
                max=num;
                id_max=i;
            } 
            else{
                bigger_before[i]=0;
                bigger_after[i]=0;
                bigger_after[id_max]+=1;
            }
        }
        while(q--){
            ll a,b;
            cin>>a>>b;
            if(b>=bigger_before[a-1]){
                if (a-1==id_max){
                    cout<<b-bigger_before[a-1]+min(bigger_before[a-1],mii)<<endl;
                }
                else{
                    cout<<min(bigger_before[a-1],mii)+min(bigger_after[a-1],b-bigger_before[a-1]+min(bigger_before[a-1],mii))<<endl;  
                }
            
            }
            else cout<<0<<endl;
        }

    }
}