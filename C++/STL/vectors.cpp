#include<iostream>
#include<vector>
#include<random>
#include<algorithm>
#include<bits/stdc++.h>

using namespace std;
void printVector(vector<int> v)
{

	while(!v.empty())
	{
		int s =v.back();
		v.pop_back();
		cout<<s<<endl;
	}

}

bool sortfunc(int i, int j)
{
	return i > j ;
}
int main()
{

	vector<int> v1;
	int n=10;
	
	while(n>0)
	{
		int val = (int) rand()%200; 
		v1.push_back(val);
		--n;
	}
	
	vector<int> v2(v1); 
	vector<int> v3;
	v3=v1; 
	sort(v1.begin(), v1.end(), sortfunc);

	cout<<"New Size of v2:"<<v2.size()<<endl;
	cout<<"New Size of v3:"<<v3.size()<<endl;
	v3.push_back(120);
	v3.push_back(12);
        cout<<endl;	
	
	sort(v3.begin(), v3.end(), [](int i, int j) -> bool
	{
		return i>j; 
	});
	
	for_each(v3.begin(), v3.end(), [](int i)
	{
		cout<<i<<" ";
	});
	cout<<endl;
		
	return 0;
}
