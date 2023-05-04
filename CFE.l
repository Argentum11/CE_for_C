%{
#include "CFE.tab.h"
#include <string.h>
%}

%%

"cout"  {return OUTPUT;}
"<<"    {return OUTPUT_OPERATOR;}
"endl"  {return NEWLINE;}
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
\n  	{return EOL;}
[0-9]+ 	{yylval = atoi(yytext);return NUMBER;}
\"[ _a-zA-z0-9\t\"\']*\" 	{
    yytext[strlen(yytext)-1]='\0';
    int i;
    for(i=0;i<strlen(yytext);i++)
    {
        yytext[i]=yytext[i+1];
    }
    for(i=0;i<strlen(yytext);i++)
    {
        if(yytext[i]=='\\')
        {
            switch(yytext[i+1])
            {
            case 'n':
                yytext[i]='\n';
                break;
            case 't':
                yytext[i]='\t';
                break;
            case '\\':
                yytext[i]='\\';
                break;
            case '\"':
                yytext[i]='\"';
                break;
            case '\'':
                yytext[i]='\'';
                break;
            case '0':   
                yytext[i]='\0';
                break;
            default:
                yytext[i]='\0';
                printf("invalid use of \\\n");
                break;
            }
            int j;
            for(j=i+1;j<strlen(yytext);j++)
            {
                yytext[j]=yytext[j+1];
            }
        }
    }
    yylval=strdup(yytext);
    return STRING;}
[(][-][0-9]+[)] 	{
    yytext[0]=' '; 
    yytext[strlen(yytext)-1]=' ';
    yylval=atoi(yytext);
    return NUMBER;}
[_a-zA-Z][_a-zA-z0-9]*	{  yylval=strdup(yytext);return VAR;}
. 	{printf("Invaild symbol %c\n",*yytext);}

%%
