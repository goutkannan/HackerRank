/***
Basic tutorial on pointer. 
Author : goutham
Reference : http://www.cplusplus.com/doc/tutorial/pointers/ 

***/

#include<iostream>
using namespace std;
// Utility function to show const pointer - read only 
void print_ptr(const int* base,int size)
{
	cout<<size<<endl;
	while(size!=0)
	{
		cout<<*base;
		base++;
		--size;
	}
	cout<<endl;
}
int ptr_size(void *ptr)
{
	return sizeof(ptr);
}

int main()
{
	int x;
	x = 12;
	// '&' operator on a basic data type prints the address associated with the variable. 
	cout<<&x<<endl;
	int *intPtr;

        //Creating a reference using pointer, making intPtr point to the address of X
        intPtr  = &x;	
	// Test the difference betwenn various pointers
	// intPtr is now the address of X and *intPtr gives us the value present in X which is called dereferencing a pointer. 

	cout<<intPtr<<'\t'<<*intPtr<<endl;
	
	// Let us move on to pointer arithmetics 
	int *ptr_as_array; 
	char *name = "Gouth";
	int array[] = { 1 , 2 , 3 , 4 , 5 };
	// Interesting point unlike a normal int, int[] can be assigned to a pointer without &. 
	// The reason is that, by default, array refers to the base address of [] 
	ptr_as_array = array;
	//We are accessing the pointers like an array using their indexes, but char* and int* sizes are different but while doing ++ we move 4 bytes for an int and 1 byte for a char. extremely usefull property. 

	for(int i=0; i<5; i++)
		cout<<*(ptr_as_array++)<<'\t'<<*(name++)<<endl;
	
	
  	//Interesting usage of Const pointers, there could be cases in which the pointers must be made read-only while passing pointers as arguments to external functions. 
	
	int size = sizeof(array)/sizeof(array[0]); // it is a method to find the size of a given array. 
	print_ptr(array,size);
	
	//Void Pointers, one of the most widely use in profressional grade softwares
	// Consider the sizeof() function it can take any pointer as a pointer, we can use a void pointer as the base and it can be casted into other types on the fly. 
	cout<<ptr_size(&x)<<endl;
	cout<<ptr_size(name)<<endl;
		

	// Curious case of Null pointers that causes Access Violation Exceptions.
	// Derefrencing nowhere(null) outside the bounds cause this exception. 
	int *null_pointer = 0;
	int *another_nullptr = NULL;
 	

	return 0;
}
