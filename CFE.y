%{
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_VAR_NUM 100
#define MAX_VAR_NAME_LEN 30
double variables[256];
typedef struct {
    char name[MAX_VAR_NAME_LEN];
    int value;
} Variable;

Variable variables[MAX_VAR_NUM];
int var_count = 0;

%}
%union {
    double dval;
    char sval;
    int a;
}

%token  NUMBER VAR
%token STORE END PRINT
%token ADD SUB MUL DIV ABS LOG
%token EOL
%token POW
%token SQRT
%token COS SIN TAN
%token MOD
%token COMMA
%token IF
%left '-' '+'
%left '*' '/' '^'
%type <dval> exp factor term
%token <dval> NUMBERS
%%


calclist:
  |calclist VAR STORE exp END EOL { 
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$2) == 0) {
                  variables[i].value = $4;
                  printf("store %s = %d\n", variables[i].name, variables[i].value);
                  found = 1;
                  break;
              }
          }
          if (!found) {
              Variable var;
              var.value = $4;
              strcpy(var.name, (char*)$2);
              variables[var_count++] = var;
              printf("store %s = %d\n", variables[var_count-1].name, variables[var_count-1].value);
          }
      }
  |calclist exp EOL{printf ("=%d\n",$2);}
  |calclist PRINT exp EOL{printf ("%d\n",$3);}
  |calclist PRINT VAR END EOL{
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$3) == 0) {
                  printf("%d\n", variables[i].value);
                  found = 1;
                  break;
              }
            }
          if (!found) {
              printf("variable %s not found\n", (char*)$3);
            }
          }
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
  |factor MOD term { $$ = fmod($1, $3); }
  ;
  
term:NUMBER {$$=$1;} 
  |LOG term { $$ = log10($2); }
  |ABS exp ABS {$$=$2>=0?$2:-$2;}
  | SQRT '(' exp ')' { $$ = sqrt($3); } 
  | COS '(' exp ')' { $$ = cos($3); } 
  | SIN '(' exp ')' { $$ = sin($3); } 
  | TAN '(' exp ')' { $$ = tan($3); }
  |'(' exp ')' { $$ = $2; }
  | VAR { $$ = variables[$1]; }
  ;
%%

main(int argc,char **argv){
	yyparse();
}

yyerror(char *s)
{
 fprintf(stderr,"error:%s\n",s);
}
