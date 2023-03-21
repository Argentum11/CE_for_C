%{
#include "CFE.tab.h"
%}

%%

"+"   	{return ADD;}
"-"   	{return SUB;}
"*"   	{return MUL;}
"/"   	{return DIV;}
"|"   	{return ABS;}
"="     {return STORE;}
";"     {return END;}
"log"   {return LOG;}
"print" {return PRINT;}
[()]    {return yytext[0]; }
[-]?[0-9]+ 	{yylval=atoi(yytext);return NUMBER;}
\n  	{return EOL;}
[ \t] 	{/*空白忽略*/}
[_a-zA-Z][_a-zA-z0-9]*	{  return VAR;}
. 	{printf("Invaild symbol %c\n",*yytext);}

%%
