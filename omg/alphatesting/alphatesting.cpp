/******************************************************************************* 
** Magnus MAGNUX Cpp source code 
** (c) Copyright 2011-2018 Magnus siiftun1857 Frankline 
** This creation is licensed under Apache License Version 2.0 
** For more information, see LICENSE 
**  
** ON GENE: 
** Filename: alphatesting.cpp 
** Date: 2018-10-22 21:34:32 
** Repository siiftun1857/workspace 
** 
** For more information, see README.MD 
** 
** Notes: 
** TODO: COMPLETE THIS 
** 
*/
#define RELEASE
//#include "MAGNUX_CORE.H" //DONT DO THIS
#include "alphatesting.h"

int main(int argc, char* argv[], char* envp[])
{
	if(argc <= 1)
	{
		cout << "Usage: alphatesting <alpha> ... " << endl;
		exit(EXIT_FAILURE);
	}
	if(argc > 2)
	{
		cout << "Warning: too many args detected, requirement is one. -- Magnus " << endl;
	}
	//end args
	
	//intake args
	const char*boo = argv[1];
	
	bool wkeeper = true;
	size_t cptr = 0;
	size_t ca_c = 0;
	size_t ca_s = 0;
	
	while(wkeeper)
	{
		switch(boo[cptr])
		{
		case '\0':
			DEBUGM("get end\n");
			wkeeper = false;
			break;
		case 'a':
			DEBUGM("get a\n");
			ca_s++;
			break;
		case 'A':
			DEBUGM("get A\n");
			ca_c++;
			break;
		default:
			DEBUGM("get blast\n");
			cout << "INPUT CORRUPTION DETECTED, please type a legal args with 'a' and 'A' only. -- Magnus " << endl;
			exit(EXIT_FAILURE);
			break;
		}
		if(ca_s>0 && ca_c>0)
		{
			wkeeper = false;
		}
		cptr ++;
	}
	
	if(ca_c>0 && ca_s==0)
	{
		cout << "A" << endl;
	}
	else if(ca_s>0 && ca_c==0)
	{
		cout << "a" << endl;
	}
	else if(ca_s>0 && ca_c>0)
	{
		cout << "0" << endl;
	}
	else 
	{
		cout << "BLANK RESULT DETECTED, what you did? -- Magnus " << endl;
		//i consider it as argv[1]==""
	}
	
	//mainexit
	exit(EXIT_SUCCESS);
	//return 0;//i will keep this for you if you just want enable it - You(aka Magnus)
}

/* eof alphatesting.cpp */

