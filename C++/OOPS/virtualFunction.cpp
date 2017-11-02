#include<iostream>
using namespace std;
/***
 * Learnings: 
 * 1. Virtual function assigned to Zero becomes a pure virtual function
 * 2. Classes the contain pure virtual functions are called abstract class
 * 3. Pure virtual functions are implemented by the derived classes of the Abstract class
 * 4. We can have pointers and references of abstract class type.
 * 5. If we do not override the pure virtual function in derived class, then derived class also becomes abstract class.
 * 6. An abstract class can have constructors.
 * 7.  Interface vs Abstract classes : Interfaces don't have implementation of functions but abstract cless  can have implementation of function other than the virtual functions. 
 * ****/

class Base
{
    protected:
        int _x;
    public:
        virtual void do_x() = 0;
        void show_x() { cout<<"...."<<_x<<"..."<<endl; }
        Base(int i) { _x = i; }
};

class Derived : public Base
{
    int _y;
    public:
        void do_x()
        {
            _x+=100;
        }
        Derived(int i,int j):Base(i) 
        {
            _y =j;
            
        }
        void show_y()
        {
             cout<<"...."<<_y<<"..."<<endl; 
        }

};
int main()
{
    Derived d(10,12);
    d.show_x();
    d.show_y();
    
    Derived *obj = new Derived(1,2);
    obj->do_x(); 
    obj->show_x();
    obj->show_y();
}
