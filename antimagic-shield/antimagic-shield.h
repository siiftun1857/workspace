#ifndef __magnualand_Antimagic_Shield__2018_1__
#define __magnualand_Antimagic_Shield__2018_1__
/*
//#
#define ANTIMAGIC_COMMENTS				1
#define ANTIMAGIC_NUMBER_SIGN			1
//|
#define ANTIMAGIC_VERTICAL_BAR			2
#define ANTIMAGIC_PIPELINE				2
// \\ 
#define ANTIMAGIC_BACKSLASH				4
//;
#define ANTIMAGIC_COMMAND_SERARATOR		8
#define ANTIMAGIC_SEMICOLON				8
//'
#define ANTIMAGIC_apostrophe			16
//"
#define ANTIMAGIC_quotation_mark		32
//`
#define ANTIMAGIC_grave_accent			64
//$
#define ANTIMAGIC_dollar_sign			128
*/
namespace magnualand
{
struct antimagicshield_setting
{
	char*target;
	char*replace;
};

const char* armorup(const char*,antimagicshield_setting setting[]);
}

#endif // ifndef __magnualand_Antimagic_Shield__2018_1__
