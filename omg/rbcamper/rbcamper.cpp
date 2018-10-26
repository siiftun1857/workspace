/******************************************************************************* 
** Magnus MAGNUX Cpp source code 
** (c) Copyright 2011-2018 Magnus siiftun1857 Frankline 
** This creation is licensed under Apache License Version 2.0 
** For more information, see LICENSE 
**  
** ON GENE: 
** Filename: rbcamper.cpp 
** Date: 2018-10-24 12:50:31 
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
#include "rbcamper.h"

#define nullptr (NULL)
#define PXMAX (10)
#define PYMAX (10)

const char* const patt="\
+____#____\
_#_#___#__\
_#_##_###_\
___#____#_\
##___##_#_\
_##_##____\
_#_____##_\
___###____\
_########_\
__@@@@@@@_\
";
enum blockt{
	UNDEF=0,
	BLANK=1,
	WALL=2,
	TARGET=3,
	SPAWN=4,
};
enum wdire {
	UP,DOWN,LEFT,RIGHT
};
wdire getL(wdire wfrom)
{
	switch(wfrom)
	{
	case UP:
		return LEFT;
	case RIGHT:
		return UP;
	case DOWN:
		return RIGHT;
	case LEFT:
		return DOWN;
	}
}
wdire getR(wdire wfrom)
{
	switch(wfrom)
	{
	case UP:
		return RIGHT;
	case RIGHT:
		return DOWN;
	case DOWN:
		return LEFT;
	case LEFT:
		return UP;
	}
}

template <typename T>
struct vector2
{
public:
	T x;
	T y;
};

blockt park[PYMAX][PXMAX]={UNDEF};
int targetslable[PYMAX][PXMAX]={0};

inline blockt getpark(int x,int y){ return park[y][x]; }
inline int gettarget(int x,int y){ return targetslable[y][x]; }


class waydump
{
public:
	wdire facing;
	wdire from;
	waydump*next_way;
	
	waydump(wdire wfrom)
	{
		from = wfrom;
		from = getR(wfrom);
		next_way = nullptr;
	}
	
	wdire turnL()
	{
		return facing = getL(facing);
	}
	
	bool ifgoesback() const
	{
		return facing == from;
	}
	
	wdire getdire() const
	{
		if(next_way==nullptr)
		{
			return facing;
		}
		return next_way->getdire();
	}
	
	int goforward()
	{
		if(next_way==nullptr)
		{
			next_way=new waydump(facing);
			return 0;
		}
		next_way->goforward();
		return 0;
	}
	int gobackward()
	{
		if(next_way==nullptr)
		{
			return 1;
		}
		if(next_way->gobackward()==1)
		{
			delete next_way;
			next_way = nullptr;
		}
		return 0;
	}
	~waydump()
	{
		delete next_way;
	}
};

class ABot{
	public:
	vector2<int> pos;
	int angle;
	blockt route[PYMAX][PXMAX];
	waydump*memdire;
	
	ABot(){
		memdire = new waydump(RIGHT);
	}
	
	vector2<int> getplus() const
	{
		vector2<int> t;
		t.x=pos.x;
		t.y=pos.y;
		switch(memdire->getdire())
		{
		case UP:
			t.y--;
			break;
		case DOWN:
			t.y++;
			break;
		case LEFT:
			t.x--;
			break;
		case RIGHT:
			t.x++;
			break;
		}
	}
	
	blockt scan()
	{
		vector2<int> t = getplus();
		if(t.x<0 || t.x>PXMAX || t.y<0 || t.y>PYMAX)
		{
			return WALL;
		}
		else
		{
			switch(getpark(t.x,t.y))
			{
			case WALL:
				return route[t.y][t.x]=WALL;
			case TARGET:
				if(gettarget(t.x,t.y)!=0)
				{
					return route[t.y][t.x]=TARGET;
				}
			case SPAWN:
			case BLANK:
				return route[t.y][t.x]=BLANK;
				break;
			case UNDEF:
			default:
				throw;
			}
		}
	}

	int run()
	{
		
	}
};

int main(int argc, char* argv[], char* envp[])
{
	if(argc <= 1)
	{
		cout << "Usage: rbcamper.cpp <sc1> <sc2> <sc3> <sc4> <sc5> <sc6> <sc7> ... " << endl;
		exit(EXIT_FAILURE);
	}
	if(argc > 8)
	{
		cout << "Warning: too many args detected, requirement is one. -- Magnus " << endl;
	}
	//end args
	
	//intake arg
	
	
	for(size_t i=0,j=0;i<PXMAX*PYMAX;j++)
	{
		switch(patt[j])
		{
		case '+':
			park[i/PXMAX][i%PXMAX]=SPAWN;
			i++;
			break;
		case '_':
			park[i/PXMAX][i%PXMAX]=BLANK;
			i++;
			break;
		case '#':
			park[i/PXMAX][i%PXMAX]=WALL;
			i++;
			break;
		case '@':
			park[i/PXMAX][i%PXMAX]=TARGET;
			i++;
			break;
		}
	}
	
	//mainexit
	exit(EXIT_SUCCESS);
	//return 0;//i will keep this for you if you just want enable it - You(aka Magnus)
}

/* eof rbcamper.cpp */
