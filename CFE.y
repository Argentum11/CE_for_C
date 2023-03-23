%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "CFE.tab.h"

double variables[256];

void yyerror(const char *s);

%}

%union {
    double dval;
    char sval;
}

%type <dval> exp factor term
%token <dval> NUMBER
%token <sval> VAR
%token STORE END PRINT
%token ADD SUB MUL DIV ABS LOG
%token EOL
%token POW
%token SQRT
%token COS SIN TAN
%token MOD
%token COMMA
%left '-' '+'
%left '*' '/' '^'

%%

calclist:
  | calclist VAR STORE exp END EOL { variables[$2] = $4; printf("store %g\n", $4); }
  | calclist exp EOL { printf("=%g\n", $2); }
  | calclist PRINT exp EOL { printf("%g\n", $3); }
  ;

exp: factor { $$ = $1; }
  | exp ADD factor { $$ = $1 + $3; }
  | exp SUB factor { $$ = $1 - $3; }
  | exp POW factor { $$ = pow($1, $3); }
  | SUB factor { $$ = -$2; }
  ;

factor: term { $$ = $1; } 
  | factor MUL term { $$ = $1 * $3; }
  | factor DIV term { $$ = $1 / $3; }
  | factor MOD term { $$ = fmod($1, $3); }
  ;

term: NUMBER { $$ = $1; }  
  | LOG term { $$ = log10($2); }
  | ABS exp ABS { $$ = $2 >= 0 ? $2 : -$2; }  
  | SQRT '(' exp ')' { $$ = sqrt($3); } 
  | COS '(' exp ')' { $$ = cos($3); } 
  | SIN '(' exp ')' { $$ = sin($3); } 
  | TAN '(' exp ')' { $$ = tan($3); } 
  | '(' exp ')' { $$ = $2; }
  | VAR { $$ = variables[$1]; }
  ;

%%

int main(int argc, char **argv) {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
