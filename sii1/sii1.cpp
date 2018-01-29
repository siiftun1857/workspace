#include <iostream>
using namespace std;
int main(int argc,char*argv[],char*envp[])
{
	cout << "argc:" << argc << endl;
	cout << "argv:" << argv << endl;
	for(int i=0;i<argc;i++)
	{
		cout << argv[i] << endl;
	}
	cout << "envp=" << envp << endl;
	for(int i=0;envp[i]!=NULL;i++)
	{
		cout << envp[i] << endl;
	}
	return 0;
}
