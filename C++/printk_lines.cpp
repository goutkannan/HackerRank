#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

int main()
{
    std::string filepath;
    int k;
    
    cin>>filepath;
    cin>>k;

    queue<string> klines; 
    ifstream ifp;
    ifp.open(filepath); 
    string line;

    for(int i =0; i< k; i++)
    {
        std::getline(ifp, line);      
        klines.push(line);
    }

    while(getline(ifp, line))
    {
        klines.pop();
        klines.push(line); 
    }

    while(!klines.empty())
    {
        cout<< klines.back();
        klines.pop(); 

    }

}


