/*
 *   Copyright (C) 2018 Magnus siiftun1857 Frankline, Magnualand, HISII. All rights reserved.
 *   FileName      :gameoflife.cpp
 *   Date          :2018-01-30
 */
#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#if defined(WINDOWS) || defined(_WIN32) || defined(_WIN64) || defined(__WIN32__)
#include <windows.h>
#endif //windows

using namespace std;
#define PARKXMAX 50
#define PARKYMAX 150
typedef bool parktype[PARKXMAX][PARKYMAX];
unsigned long long int reset_count=0;
parktype park={0};
parktype parkbuffer={0};
parktype parkhis1={0};
parktype parkhis2={0};
bool nexthis1 = true;
int record_seed = 0;
size_t record_count = 0;

/*      x-1
 *       ^
 *     1 2 3
 * y-1 8   4 y+1
 *     7 6 5
 *       v
 *      x+1
 */
inline bool lookaround(int x,int y,char dire)//get neighbour cell stat
{

	if(dire==1||dire==2||dire==3)
		x--;
	else if(dire==5||dire==6||dire==7)
		x++;

	if(dire==3||dire==4||dire==5)
		y++;
	else if(dire==1||dire==7||dire==8)
		y--;

	if(x>=PARKXMAX)
		x=0;
	else if(x<0)
		x=PARKXMAX-1;
	if(y>=PARKYMAX)
		y=0;
	else if(y<0)
		y=PARKYMAX-1;

	return park[x][y];
}
inline bool testfor(int x,int y)//check the cell stat
{
	char ner=0;
	for(int i=1;i<9&&ner<4;i++)
	{
		if(lookaround(x,y,i))
			ner++;
	}
	if(ner==2)
		return park[x][y];	//rule:keep stat when 2 nei
	if(ner==3)
		return true;		//rule:alive when 3 nei
	return false;			//rule:dead by lonely or crowd
}

int main_game(int argc,char*argv[],char*envp[])
{
#if defined(WINDOWS) || defined(_WIN32) || defined(_WIN64) || defined(__WIN32__)
	HANDLE hdout = GetStdHandle(STD_OUTPUT_HANDLE);
#endif //windows
	size_t count=0;
	int seed=0;
	bool ifdead=false;
	//seed the park
	if(argc>1)//if argv[1] is exist, srand by it
	{
		sscanf(argv[1],"%d",&seed);
		srand(seed);
	}
	else//srand by the time
	{
		srand(seed=time(NULL));
	}
	for(int i=0;i<PARKXMAX;i++)
	{
		for(int j=0;j<PARKYMAX;j++)
		{
			park[i][j]=!((bool)(rand()%4));// 1/4 of the park has live cell
		}
	}
	//star the game
	while(true)
	{
		//record
		if(count>record_count)
		{
			record_count=count;
			record_seed=seed;
		}
		//print title
		cout << "\033c" << "Game of life by Magnussiiftun1857" << " reset:" << reset_count << " record:" << record_seed << "-" << record_count << " seed:" << seed << " count:" << count++ <<endl;
//#define printdisable
#ifndef printdisable
		//print the park
		for(int i=0;i<PARKXMAX;i++)
		{
			cout << "    " ;
			for(int j=0;j<PARKYMAX;j++)
			{
#if defined(__linux__) || defined(__linux)
				cout << ((park[i][j]==true)?"\e[42m#\e[0m":"\e[0m-\e[0m");
#endif //linux
#if defined(WINDOWS) || defined(_WIN32) || defined(_WIN64) || defined(__WIN32__)
				if(park[i][j]==true)
				{
					SetConsoleTextAttribute(hdout, BACKGROUND_GREEN | BACKGROUND_INTENSITY| FOREGROUND_INTENSITY);
					cout << "#";
				}
				else
				{
					SetConsoleTextAttribute(hdout, BACKGROUND_BLUE | BACKGROUND_GREEN | BACKGROUND_RED | BACKGROUND_INTENSITY | FOREGROUND_INTENSITY);
					cout << ".";
				}
#endif //windows
			}
			cout << endl;
		}
#endif // !printdisable
		//testfor every cell
		for(int i=0;i<PARKXMAX;i++)
		{
			for(int j=0;j<PARKYMAX;j++)
			{
				parkbuffer[i][j]=testfor(i,j);
			}
		}
		//sync the park
		ifdead=true;
		for(int i=0;i<PARKXMAX;i++)
		{
			for(int j=0;j<PARKYMAX;j++)
			{
				park[i][j]=parkbuffer[i][j];
				if(nexthis1)//check and write to parkhis
				{
					if(parkhis1[i][j]!=park[i][j])
					{
						ifdead=false;
						parkhis1[i][j]=park[i][j];
					}
				}
				else
				{
					if(parkhis2[i][j]!=park[i][j])
					{
						ifdead=false;
						parkhis2[i][j]=park[i][j];
					}
				}
			}
		}
		//gameover if stagnate
		if(ifdead)
			return 0;
		nexthis1=!nexthis1;
#ifndef printdisable
		usleep(50000);
#endif // !printdisable
	}
	return 0;
}

int main(int argc,char*argv[],char*envp[])
{
	while(true)
	{
		main_game(argc,argv,envp);
		reset_count++;//add a reset count
	}
	return 0;
}

