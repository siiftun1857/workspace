#include <iostream>
#include <stdint.h>
using namespace std;
uint32_t fun(uint32_t a, uint32_t b)
{
    while (true)
    {
		if(a == b)
			return a;
		else if(a > b)
			a = a % b;
		else if(a < b)
			b = b % a;
		if(b == 0)
    		return a;
		if(a == 0)
    		return b;
    }
}

int main()
{
	cout<<fun(16,32)<<endl;
}
