%{
#include "CFE.tab.h"
%}

%%

"+"   	{return ADD;}
"-"   	{return SUB;}
"*"   	{return MUL;}
"/"   	{return DIV;}
"^"     {return POW;}
"|"   	{return ABS;}
"="     {return STORE;}
";"     {return END;}
"sqrt"  {return SQRT;}
"cos"   {return COS;}
"sin"   {return SIN;}
"tan"   {return TAN;}
"log"   {return LOG;}
"%"     {return MOD;}
"print" {return PRINT;}
[()]    {return yytext[0]; }
[0-9]+(\.[0-9]+)? { yylval.dval = atof(yytext); return NUMBER; }
\n  	{return EOL;}
[ \t] 	{/*空白忽略*/}
[_a-zA-Z][_a-zA-z0-9]*	{  return VAR;}
. 	{printf("Invaild symbol %c\n",*yytext);}

%%
