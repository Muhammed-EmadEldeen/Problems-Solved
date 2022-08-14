#include<iostream>
#include<cmath>
#define ll long long
using namespace std;

int main(){
    ll t;
    cin>>t;
    while(t--){
        ll n,m;
        cin>>n>>m;
        ll min_tasks = ceil(m/n);
        ll count=min_tasks;
        ll list[m];
        for (ll i=0;i<m;i++){
            cin>>list[i];
        }
        ll workers[n];
        for (ll i=0;i<m;i++){
            workers[list[i]-1]+=1;
        }
        for(ll i=0;i<n;i++){
            ll j=workers[i];
            if(j>=min_tasks) count+=j-min_tasks;
            else if(j+2<=min_tasks) count-= floor((min_tasks-j)/2);
        }   
        cout<<count<<endl;
    }
}