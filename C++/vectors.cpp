#include<iostream>
#include<vector>
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
int main()
{

	vector<int> v1 = {12,23,45};
	for(int a : v1)
		cout<<a<<"...";
	
	cout<<"\n";

	v1.push_back(11);
	v1.push_back(24);
//	v1.insert(3,99);

	printVector(v1);
	cout<<"New Size :"<<v1.size()<<endl;

return 0;
}
