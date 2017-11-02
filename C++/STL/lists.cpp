#include<iostream>
#include<list>
#include<iterator>
#include<random> 
using namespace std;
void prinlist(list<int> dll)
{

	list<int> :: iterator it;
	for(it = dll.begin(); it != dll.end(); ++it)
		cout<<*it<<" --> ";

	cout<<endl;  

}

bool randomlist(list<int> &dll, int size)
{
	try 
	{
		for(int i=0;i<size;++i)
			dll.push_back(rand()%(size*100));
	
	}
	catch(...) 
	{
		return false;
	}


	return true;
}
int main()
{
	list<int> dll1;
	list<int> dll2; 
	
	int n = 10;
	
	randomlist(dll1,n);
	randomlist(dll2,n);

	prinlist(dll1);
	
	dll1.push_front(10);
	prinlist(dll1);
cout<<"//Pop front"<<endl; 
	dll1.pop_front();
	prinlist(dll1);
/*cout<<"//pop back"<<end; 
	dll1.pop_back();
	prinlist(dll1);*/
list<int>::iterator pos = dll1.begin();
cout<<"//Emplace insert"<<endl;
	advance(pos,3);
	dll1.emplace(pos ,-1);
	prinlist(dll1);	


cout<<"//Reverse a list"<<endl;
	dll1.reverse();
	prinlist(dll1);
cout<<"//Sort "<<endl;
	dll1.sort();
	dll2.sort();
	prinlist(dll1);
	
cout<<"//Merge"<<endl;
	dll1.merge(dll2);
	prinlist(dll1);

return 0;


}
