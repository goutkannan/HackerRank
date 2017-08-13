/**
C++ doesn't have explicit garbage collector. Hence all the pointers declared using 
new operartor has to be removed using delete()

Inorder to avoid  explicit deletes, smart pointer can be wrapper class for pointers
and the destructor for that class do delete. 

It is very powerfull method that are used by shared_pointer, weak_pointer etc.

**/

#include<iostream>
using namespace std;
 template <class T>
 class smartPtr {
    T *ptr;
    public:
        explicit smartPtr(T *p=NULL) 
        {
            ptr = p;
        }
        ~smartPtr() 
        {
            delete(ptr); 
        }
        // Overloading dereferncing operator
        T & operator *() {  
        cout<<"Test..."<<endl; 
        return *ptr; 
        }
 
   // Overloding arrow operator so that members of T can be accessed
   // like a pointer (useful if T represents a class or struct or 
   // union type)
         T * operator -> () { return ptr; }
 };
 int main()
 {
     cout<<"Why";
     smartPtr<float> obj(new float());
     *obj = 20.02;

    
     cout << *obj;
     
     return 0; 
 }