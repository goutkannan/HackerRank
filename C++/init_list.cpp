#include<iostream>
using namespace std;
class test
{

	const int val;
	public:
	test(int t):val(t)
	{ 
		cout<<this->val<<endl;
	}

};

int main()
{
	test obj(10);
	
}

