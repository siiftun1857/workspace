#include <iostream>
using namespace std;

int foo(int vel)
{	
	if(vel<=0)//x<=0
	{return 7*vel+10;}
	else if(vel<=10)//0<x<=10
	{return 3*vel*vel;}
	else if(vel<=20)//10<x<=20
	{return -vel;}
	else//x>20
	{return 30;}
}

int main(int argv, char*argc[], char*envp[])
{
	int vel = 0;
//	int ret = 0;
	
	if(argv<=1)
	{
		cout << "Usage: 4-3-9 <number> ..." << endl;
		return -1;;
	}
	
	sprintf(argc[1],"%d",vel);

	cout << "Output :" << foo(vel) << endl;

	return 0;
}
