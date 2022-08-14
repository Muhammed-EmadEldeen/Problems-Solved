#include<iostream>
#define ll long long 

using namespace std;

int main(){
    ll t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        ll previous_num=0;
        bool answer1=true;
        bool answer2=true;
        ll list[n];
        for(ll i=0;i<n;i++){
            cin>>list[i];
        }
        for(ll i=0; i<n-1; i++){
            ll num;
            num=list[i];
            if(num>=previous_num){
                previous_num=num;
            }
            else{
                answer1=false;
                break;
            }
        }
        if (!answer1){
            ll j=n-1;
            ll previouss_num=0;
            for(j;j>0;j--){
                ll num;
                num=list[j];
                if (num>=previouss_num){
                    previouss_num=num;
                }
                else{
                    answer2=false;
                    break;
                }
            }
        }
        if(answer1 || answer2){
            cout<<"YES"<<endl;

        }
        else cout<<"NO"<<endl;
    }
    return 0;
}