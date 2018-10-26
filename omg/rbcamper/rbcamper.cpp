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
inline wdire getL(wdire wfrom)
{
	switch(wfrom)
	{
	case UP:
		return LEFT;
	case LEFT:
		return DOWN;
	case DOWN:
		return RIGHT;
	case RIGHT:
		return UP;
	}
}
inline wdire getR(wdire wfrom)
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
inline string wdireToString(wdire wfrom)
{
	/*switch(wfrom)
	{
	case UP:
		return "UP";
	case LEFT:
		return "LEFT";
	case DOWN:
		return "DOWN";
	case RIGHT:
		return "RIGHT";
	}*/
	switch(wfrom)
	{
	case UP:
		return "^";
	case LEFT:
		return "<";
	case DOWN:
		return "v";
	case RIGHT:
		return ">";
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
inline int taketarget(int x,int y)
{
	if(getpark(x,y)==TARGET && targetslable[y][x]!=0)
	{
		int ret = targetslable[y][x];
		targetslable[y][x]=0;
		return ret;
	}
	else
		throw;
}


class waydump
{
public:
	wdire facing;
	wdire from;
	waydump*next_way;
	bool isroot;
	
	waydump(wdire wfrom)
	{
		from = getR(getR(wfrom));
		facing = getR(wfrom);
		next_way = nullptr;
		isroot = false;
	}
	
	waydump(wdire wfrom, bool ifroot)
	{
		from = getR(getR(wfrom));
		facing = getR(wfrom);
		next_way = nullptr;
		isroot = ifroot;
	}
	
	size_t depth() const
	{
		if(next_way==nullptr)
		{
			return 1;
		}
		return next_way->depth()+1;
	}
	
	vector2<int> posdump() const
	{
		vector2<int> retpos={0,0};
		switch(from)
		{
		case UP:
			retpos.y++;
			break;
		case DOWN:
			retpos.y--;
			break;
		case LEFT:
			retpos.x++;
			break;
		case RIGHT:
			retpos.x--;
			break;
		}
		if(next_way!=nullptr)
		{
			vector2<int> tempos = next_way->posdump();
			retpos.x+=tempos.x;
			retpos.y+=tempos.y;
		}
		return retpos;
	}
	
	wdire turnL()
	{
		if(next_way==nullptr)
		{
			return facing = getL(facing);
		}
		return next_way->turnL();
	}
	
	wdire turnR()
	{
		if(next_way==nullptr)
		{
			return facing = getR(facing);
		}
		return next_way->turnR();
	}
	
	wdire turnto(wdire to)
	{
		if(next_way==nullptr)
		{
			return facing = getR(to);
		}
		return next_way->turnto(to);
	}
	
	bool ifgoesback() const
	{
		if(next_way==nullptr)
		{
			return facing == from;
		}
		return next_way->gobackward();
	}
	
	wdire getdire() const
	{
		if(next_way==nullptr)
		{
			return facing;
		}
		return next_way->getdire();
	}
	
	wdire getfrom() const
	{
		if(next_way==nullptr)
		{
			return from;
		}
		return next_way->getfrom();
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
	size_t score;
	size_t angle;
	blockt route[PYMAX][PXMAX];
	waydump*memdire;
	
	ABot(){
		memdire = new waydump(RIGHT);
	}
	
	vector2<int> getpos()
	{
		vector2<int> tempos = memdire->posdump();
		tempos.x--;
		return tempos;
	}
	
	vector2<int> syncpos()
	{
		return pos=getpos();
	}
	
	vector2<int> getplus()
	{
		syncpos();
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
		if(t.x<0 || t.y<0 || t.x>PXMAX || t.y>PYMAX)
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
	
	bool grab()
	{
		vector2<int> t = getplus();
		if(t.x<0 || t.x>PXMAX || t.y<0 || t.y>PYMAX)
		{
			return false;
		}
		else
		{
			switch(getpark(t.x,t.y))
			{
			case TARGET:
				if(gettarget(t.x,t.y)!=0)
				{
					score+=taketarget(t.x,t.y);
					return true; 
				}
			default:
				return false;
			}
		}
	}
	void output()
	{
		cout<<"depth: "<<memdire->depth()<<", x: "<<getpos().x<<", y: "<<getpos().y<<", from: "<<wdireToString(memdire->getfrom())<<", facing: "<<wdireToString(memdire->getdire())<<". "<<endl;
	}
	
	int step()
	{
		blockt scanresult=scan();
		switch(scanresult)
		{
			case WALL:
				cout<<"WALL";
				memdire->turnL();
				if(memdire->ifgoesback())
				{
					memdire->gobackward();
					memdire->turnL();
				}
				return 0;
			case TARGET:
				return -1;
			case SPAWN:
			case BLANK:
				cout<<"BLANK";
				memdire->goforward();
				return 0;
				break;
			case UNDEF:
			default:
				throw;
		}
	}
	
	int run()
	{
		int stepresult=0;
		output();
		while(true)
		{
			stepresult=step();
			output();
			if(stepresult==-1)
				break;
		}
	} 
};

int main(int argc, char* argv[], char* envp[])
{
	
	if(argc <= 1)
	{
		cout << "Usage: rbcamper.cpp <sc1> <sc2> <sc3> <sc4> <sc5> <sc6> <sc7> ... " << endl;
		//exit(EXIT_FAILURE);
	}
	if(argc > 8)
	{
		cout << "Warning: too many args detected, requirement is 7. -- Magnus " << endl;
	}
	//end args
	
	//intake arg
	
	ABot aibot1;
	ABot aibot2;
	
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
	cout<<"Map output: "<<endl;
	for(size_t k=0;k<PXMAX*PYMAX;k++)
	{
		switch(park[k/PXMAX][k%PXMAX])
		{
		case SPAWN:
			cout<<"+";
			break;
		case BLANK:
			cout<<"_";
			break;
		case WALL:
			cout<<"#";
			break;
		case TARGET:
			cout<<"@";
			break;
		}
		if(k%PXMAX==PXMAX-1)
			cout<<endl;
	}
	cout<<endl;
	
	aibot1.output();
	aibot1.run();
	
	
	//mainexit
	exit(EXIT_SUCCESS);
	//return 0;//i will keep this for you if you just want enable it - You(aka Magnus)
}

/* eof rbcamper.cpp */
