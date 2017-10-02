#include<iostream>
using namespace std;
class baseA {
	public:
virtual void display()=0; 
};

class derivedA:public baseA 
{

	public:
	void display() { cout<<"Banner Derived"<<endl; }
};




int main()
{
	baseA *ptr = new derivedA();
	ptr->display();
	return 0;
}
