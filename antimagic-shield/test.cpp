#include <iostream>
#include <cstdio>
#include <string>
#include <stdlib.h>
using namespace std;
int main(int argc,char*argv[],char*envp[])
{
//	long commax=sysconf(_SC_ARG_MAX);
	if(argc <= 1)
	{
		cout << "Usage: " << argv[0] << " <string> ..." << endl;
		return -1;
	}
	string temp = "\0";
	for(int i=1;argv[i]!=NULL;i++)
	{
		temp = "echo '";
		for(int j=0;argv[i][j]!=0;j++)
		{
			if(argv[i][j]=='\\' || argv[i][j]=='\'')
			{
				temp += '\\';
			}
			temp += argv[i][j];
		}
		temp += '\'';
		system(temp.c_str());
	}
	return 0;
}
//#error
