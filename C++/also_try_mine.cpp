#include<iostream>
#define ll long long
using namespace std;

int main(){

    ll n,m;
    cin>>n>>m;
    ll main_list[n];
    for(ll i=0;i<n;i++) cin>>main_list[i];
    ll left_to_right[n];
    ll right_to_left[n];
    left_to_right[0]=0;
    right_to_left[n-1]=0;

    for(ll i=1;i<n;i++){
        ll a=main_list[i-1]-main_list[i];
        if(a>0){
            left_to_right[i]=left_to_right[i-1]+a;
        }
        else{
            left_to_right[i]=left_to_right[i-1];
        }
    }
    for(ll i=n-1;i>=0;i--){
        ll a=main_list[i]-main_list[i-1];
        if(a>0){
            right_to_left[i-1]=right_to_left[i]+a;
        }
        else{
            right_to_left[i-1]=right_to_left[i];
        }
    }
    while(m--){
        ll s,e;
        cin>>s>>e;
        if(e>s){
            cout<<left_to_right[e-1]-left_to_right[s-1]<<endl;
        }
        else{
            cout<<right_to_left[e-1]-right_to_left[s-1]<<endl;
        }
    }
}