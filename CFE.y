%{
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "CFE.tab.h"
#include <ctype.h>
#include <math.h>

#define MAX_VAR_NUM 100
#define MAX_VAR_NAME_LEN 30
int flag1;


typedef struct {
    char name[MAX_VAR_NAME_LEN];
    double value;
} Variable;

Variable variables[MAX_VAR_NUM];
int var_count = 0;

%}

%token  NUMBER VAR STRING
%token STORE END PRINT
%token ADD SUB MUL DIV ABS LOG
%token OUTPUT OUTPUT_OPERATOR NEWLINE EOL 
%token BIGGER
%token SMALLER
%token BIGEQUAL
%token SMALLEQUAL
%token EQUAL
%token POW
%token SQRT
%token COS SIN TAN
%token MOD
%token IF ELSE LBRACE RBRACE

%left '-' '+'
%left '*' '/' '^'
%%


calclist:
  |calclist VAR STORE exp END EOL { 
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$2) == 0) {
                  variables[i].value = $4;
                  printf("store %s = %lf\n", variables[i].name, variables[i].value);
                  found = 1;
                  break;
              }
          }
          if (!found) {
              Variable var;
              var.value = $4;
              strcpy(var.name, (char*)$2);
              variables[var_count++] = var;
              printf("store %s = %lf\n", variables[var_count-1].name, variables[var_count-1].value);
          }
      }
  | calclist IF '(' exp ')' LBRACE OUTPUT output_item END RBRACE EOL
    { if ($3 > 0) { yyparse(); } }
  | calclist if_stmt EOL {}
  |calclist OUTPUT output_item END EOL{}
  ;

output_item:OUTPUT_OPERATOR exp{if(flag1!=0){printf ("%d",$2);}flag1=1;}
  |OUTPUT_OPERATOR STRING{printf ("%s",$2);}
  |OUTPUT_OPERATOR NEWLINE{printf ("\n");}
  |output_item OUTPUT_OPERATOR exp{if(flag1!=0){printf ("%d",$2);}flag1=1;}
  |output_item OUTPUT_OPERATOR STRING{printf ("%s",$3);}
  |output_item OUTPUT_OPERATOR NEWLINE{printf ("\n");}
  ;
if_stmt:
  IF '(' exp ')' LBRACE calclist RBRACE
    { if ($3 <= 0) { yyparse(); flag1=0;} }
  | IF '(' exp ')' LBRACE calclist RBRACE ELSE LBRACE calclist RBRACE
    { if ($3 > 0) { yyparse(); } else { yyparse(); } }
  | IF '(' exp ')' LBRACE calclist RBRACE
    { if ($3 > 0) { yyparse(); } }
  | IF '(' exp ')' LBRACE calclist RBRACE ELSE LBRACE calclist RBRACE
    { if ($3 > 0) { yyparse(); } else { yyparse(); } }
  ;


exp:factor {$$ = $1;}
  |exp ADD factor{$$=$1+$3;}
  |exp SUB factor{$$=$1-$3;}
  |exp POW factor { $$ = pow($1, $3); }
  |SUB factor{$$=-$2;}
  ;

factor:term {$$=$1;}
  |factor MUL term{$$=$1*$3;}
  |factor DIV term{$$=$1/$3;}
  | factor MOD term { $$ = fmod($1, $3); }
  | factor BIGGER term { $$ = $1 > $3 ? 1 : 0; }
  | factor SMALLER term { $$ = $1 < $3 ? 1 : 0; }
  | factor BIGEQUAL term { $$ = $1 >= $3 ? 1 : 0; }
  | factor SMALLEQUAL term { $$ = $1 <= $3 ? 1 : 0; }
  | factor EQUAL term { $$ = $1 == $3 ? 1 : 0; }
  ;
  
term:NUMBER {$$=$1;}
  |VAR { 
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$1) == 0) {
                  $$ = variables[i].value;
                  
                  found = 1;
                  break;
              }
          }
          if (!found) {
              printf("variable %s not found\n", (char*)$1);
          }
      }
  |LOG term {$$ = log($2);}
  |ABS exp ABS {$$=$2>=0?$2:-$2;}
  | SQRT '(' exp ')' { $$ = sqrt($3); }
  | COS '(' exp ')' { $$ = cos($3); }
  | SIN '(' exp ')' { $$ = sin($3); }
  | TAN '(' exp ')' { $$ = tan($3); }
  |STRING {$$=$1;}
  |'(' exp ')' { $$ = $2; }
  ;
%%

main(int argc,char **argv){
	yyparse();
}

yyerror(char *s)
{
 fprintf(stderr,"error:%s\n",s);
}
