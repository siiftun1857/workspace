/******************************************************************************* 
** Magnus MAGNUX Cpp source code 
** (c) Copyright 2011-2018 Magnus siiftun1857 Frankline 
** This creation is licensed under Apache License Version 2.0 
** For more information, see LICENSE 
**  
** ON GENE: 
** Filename: funnnn.cpp 
** Date: 2018-10-22 22:50:01 
** Repository siiftun1857/workspace 
** 
** For more information, see README.MD 
** 
** Notes: 
** TODO: COMPLETE THIS 
** 
*/
#define DEBUG
//#include "MAGNUX_CORE.H" //DONT DO THIS
#include "funnnn.h"

uint32_t fun(uint32_t p, uint32_t k)
{
	if(p > 0)
	{
		k = fun(k % p, p);
	}
	return k;
}

int main(int argc, char* argv[], char* envp[])
{
	/*if(argc <= 2)
	{
		cout << "Usage: funnnn <numk> <num> [num] an most 256 input ... " << endl;
		exit(EXIT_FAILURE);
	}
	//end args
	
	//intake args
	int space[256]={0};
	for(int i=1;i<argc-1;i++)
	{
		sscanf(argv[i],"%d",&(space[i]));
		cout<<space[i]<<endl;
	}
	
	for(int j=2;j<argc;j++)
	{
		cout << fun(space[j],space[1]);
	}*/
	
	cout << fun(1,7)<<endl;
	cout << fun(2,7)<<endl;
	cout << fun(3,7)<<endl;
	cout << fun(4,7)<<endl;
	cout << fun(5,7)<<endl;
	cout << fun(6,7)<<endl;
	cout << fun(7,7)<<endl;
	cout << fun(8,7)<<endl;
	cout << fun(9,7)<<endl;
	cout << fun(10,7)<<endl;
	
	//mainexit
	exit(EXIT_SUCCESS);
	//return 0;//i will keep this for you if you just want enable it - You(aka Magnus)
}

/* eof funnnn.cpp */

