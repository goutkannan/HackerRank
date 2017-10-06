#include<iostream>
#include<string>
using namespace std;
class Car {
    private:
	string vin;
	string make;
	string model;
	int fuel_capacity;
	float max_speed;
	int max_RPM;
    public:
	//Default Constructor as we have our own copy constructor
	Car() {}
	// usually done in a constructor but using setter to acheive that
	void setValue(string vin, string make, string model, int fuel, int speed, int maxRPM)
	{
		this->vin = vin;
		this->make = make;
		this->model = model;
		this->fuel_capacity = fuel;
		this->max_speed = speed;
		this->max_RPM = maxRPM;
	
	}
	// implementation on of deep copy using copy constructor	
	Car(const Car &obj)
	{
		this->vin = obj.vin;
		this->make = obj.make;
		this->model =obj.model;
		this->fuel_capacity = obj.fuel_capacity;
		this->max_speed = obj.max_speed;
		this->max_RPM = obj.max_RPM;
		
	}
	//Stealing the idea from python 
	void __repr__()
	{
		cout<<"The car with vin "<<this->vin<<" is a "<<this->make<<" "<<this->model<<endl;
	}
	void updatetonew(string newmodel)
	{
		this->model = newmodel;
	}
	
};

int main()
{
	Car vehicle1;
	vehicle1.setValue("xxx123xxx","BMW","A8",1200,220,4500);
	//Display the details
	vehicle1.__repr__();
	//Copy Constructor usage 
	
	Car tmp_object(vehicle1);
	tmp_object.updatetonew("A10");
	cout<<"tmp object"<<endl;
	tmp_object.__repr__();
	cout<<"main object"<<endl;
	vehicle1.__repr__();
}
