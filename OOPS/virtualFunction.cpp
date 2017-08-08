#include<iostream>
using namespace std;
class Base
{
    int _x;
    public:
        virtual void do_x() = 0;
        void show_x() { cout<<"...."<<_x<"..."<<endl; }
        Base(int i) { _x = i; }
};

class Derived : public base
{
    int _y;
    public:
        Derived(int i,int j):Base(i) 
        {
            _y =j;
            
        }
        void show_y()
        {
             cout<<"...."<<_y<"..."<<end; 
        }

};
int main()
{
    Derived d(10,12);
    d.show_x();
    d.show_y();

}