#include<iostream>
#include<map>
#include<iterator>
#include<vector>

using namespace std;

int main()
{
	map<int, int> hashMap; 
	
	map<int,int>::iterator entry;

	vector<int> number;
	number.push_back(10);
	number.push_back(2);
	number.push_back(13);
	number.push_back(-1);
	number.push_back(5);
	number.push_back(20);
	number.push_back(7);
	number.push_back(9);
	number.push_back(12);

	int sum =12;
	hashMap.insert(std::pair<int,int>(sum - *number.begin(), *number.begin()));

	for(vector<int>::iterator it= number.begin()+1; it !=number.end(); ++it)
	{
		entry = hashMap.find(*it);
		if (entry == hashMap.end())
		{
			hashMap.insert(std::pair<int,int>(sum -(*it), *it));
		
		}	
		else
			cout<<entry->first<<" + " <<entry->second<<endl;	
		
	}
	return 0;
}

