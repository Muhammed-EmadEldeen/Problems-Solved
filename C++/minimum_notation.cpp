#include<iostream>
#include<bits/stdc++.h> 
#include<string>
#define ll long long 


using namespace std;

void solve();

int main(){
	ll t;
	cin>>t;
	while(t--){
		solve();
		cout<<endl;
	}
		
}
void solve(){
	int answer[10]={0};
	string number;
	cin>>number;
	ll n=number.size();
	vector<int> numbers;
	for(ll i=0;i<n;i++){
		numbers.push_back(number[i]-'0');
	}
	int smallest_num=9;
	ll i=n-1;
	while(i>=0){
		if(numbers[i]<=smallest_num){
			smallest_num=numbers[i];
			answer[numbers[i]]++;
			}

		else{
			answer[min(numbers[i]+1,9)]++;
			}
			
		i--;
		}	

	
	for(int k=0;k<10;k++){
		int times = answer[k];
		while(times){
			cout<<k;
			times--;
		}
	}

}
	
