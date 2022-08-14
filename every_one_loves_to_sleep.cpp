#include<iostream>

using namespace std;

int main(){

    int t;
    cin>>t;
    while(t--){
        int n,h,m;
        cin>>n>>h>>m;
        int min_hour=23;
        int min_minute=59;
        int hi,mi;
        while(n--){
            int ansh,ansm;
            cin>>hi>>mi;
            if (mi<m){
                ansm=(mi-m)%60;
                ansh=(hi-h-1)%24;
            }
            else{
                ansm=mi-m;
                ansh=(hi-h)%24;
            }

            if(ansh<min_hour){
            min_hour=ansh;
            min_minute=ansm;
            }
            else if(ansh==min_hour && ansm<min_minute) min_minute=ansm;
        }
        cout<<min_hour<<" "<<min_minute<<endl;
    }
}