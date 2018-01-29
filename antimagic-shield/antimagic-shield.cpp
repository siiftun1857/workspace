#include "antimagic-shield.h"
#include <string>
using namespace std;
namespace magnualand
{
const char*armorup(const char*input,const antimagicshield_setting*setting[])
{
	string output = "\0";
	for(int j=0;input[j]!=0;j++)
	{
		for(int i=0;setting[i]==NULL;i++)
		{
			if(input[j]==setting[i]->target)//ERROR
			{
				output += setting[i]->replace;
			}
			else
			{
				output += input[j];
			}
		}
	}
	return output.c_str();
}
}
