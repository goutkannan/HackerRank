#include<iostream>
#include<fstream>
#include<set>
#include<algorithm>
using namespace std;
int uniquewords(ifstream &ifp, set<string> &unique)
{
	string word;
	while(ifp >> word)
	{
		std::replace_if(word.begin(), word.end(), ::ispunct, '\0');
		unique.insert(word);

	}	
	return unique.size();
}
int words_that_occur_once(ifstream &ifp, set<string> &unique)
{
	cout<<"in"<<endl;
	string word;
        set<string> found_set;
	while(ifp >> word)
	{
	  if(found_set.count(word) == 0)
	  {
	       
		std::remove_if(word.begin(), word.end(), ::ispunct);
		found_set.insert(word);
		unique.insert(word);
	
	  }
	  else
	  {
		unique.erase(word);
		
	  }
	}
	
	return unique.size();
}

int main()
{
	set<string> words;
	set<string> unique_words;
	ifstream ifp;
	ifp.open("data.txt");

	int count = uniquewords(ifp, words);
	cout<<"Number of unique words "<<count<<endl;
        cout<<"Test check"<< words.size()<<endl;	
        ifp.close();

	ifp.open("data.txt");
	cout<<"Number of words that occur once:"<<words_that_occur_once(ifp, unique_words);
	for(set<string>::iterator it = unique_words.begin(); it != unique_words.end(); ++it)
		cout<<*it<<endl;

	cout<<endl;
	ifp.close();
	return 0;
}
