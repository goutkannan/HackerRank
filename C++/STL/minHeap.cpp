#include <bits/stdc++.h>
using namespace std;
class Comp {
  private:
	double real;
	double img;
  public:
	Comp(double _r, double _i)
	{
		real = _r;
		img  = _i;
	}
	double r() { return real; }
	double i() { return img; }

};

class myabs {
public:
    double operator() ( Comp& p1,  Comp& p2)
    {
        return (p1.r()*p1.r() + -1*p1.i()*p1.i()) > (p2.r()*p2.r() + -1* p2.i()*p2.i());
    }

};
// Driver co_i;de
int main ()
{
    // Creates a max heap
    priority_queue <Comp, vector<Comp>, myabs > pq;
    pq.push(Comp(5,2));
    pq.push(Comp(12,10));
    pq.push(Comp(10,1));
    pq.push(Comp(30,14));
    pq.push(Comp(20,1));
 
    // One by one extract items from max heap
    while (pq.empty() == false)
    {
	Comp c = pq.top();
        cout << c.r() << " +i"<< c.i()<<endl;
        pq.pop();
    }
	cout<<endl; 
    return 0;
}
