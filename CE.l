%{
#include "CFE.tab.h"
#include <string.h>
#include <stdio.h>
%}


%%

"cout"  {return OUTPUT;}
"<<"    {return OUTPUT_OPERATOR;}
"endl"  {return NEWLINE;}
"int"   {return TYPE_INT;}
"double"    {return TYPE_DOUBLE;}
"string"    {return TYPE_STRING;}
"+"   	{return ADD;}
"-"   	{return SUB;}
"*"   	{return MUL;}
"/"   	{return DIV;}
"^"     {return POW;}
"|"   	{return ABS;}
"="     {return STORE;}
";"     {return END;}


">"     {return BIGGER;}
"<"     {return SMALLER;}
">="     {return BIGEQUAL;}
"<="     {return SMALLEQUAL;}
"=="     {return EQUAL;}
"sqrt"  {return SQRT;}
"cos"   {return COS;}
"sin"   {return SIN;}
"tan"   {return TAN;}
"log"   {return LOG;}

"if" { return IF; }
"else" { return ELSE; }

"{" { return LBRACE; }
"}" { return RBRACE; }
"%"     {return MOD;}
"print" {return PRINT;}
[()]    {return yytext[0]; }
[0-9]+ 	{yylval.num = atof(yytext);return NUMBER;}
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
    yylval.str=strdup(yytext);
    return STRING;}
[(][-][0-9]+[)] 	{
    yytext[0]=' '; 
    yytext[strlen(yytext)-1]=' ';
    yylval.num=atof(yytext);
    return NUMBER;}
[0-9]+\.[0-9]+ 	{yylval.num=atof(yytext);return NUMBER_DOUBLE;}
[(][-][0-9]+\.[0-9]+[)] {
    yytext[0]=' '; 
    yytext[strlen(yytext)-1]=' ';
    yylval.num=atof(yytext);
    return NUMBER_DOUBLE;
}
[_a-zA-Z][_a-zA-z0-9]*	{  yylval.str=strdup(yytext);return VAR;}
\n  	{return EOL;}
[ \t] 	{/*空白忽略*/}
. 	{printf("Invaild symbol %c\n",*yytext);}

%%
