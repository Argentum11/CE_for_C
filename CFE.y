%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "CFE.tab.h"
#include <ctype.h>

double variables[256];

void yyerror(const char *s);

%}

%union {
    double dval;
    char sval;
    int a;
    int ival;
}

%type <dval> exp factor term
%token <dval> NUMBER
%token <sval> VAR
%token STORE END PRINT
%token BIGGER
%token SMALLER
%token ADD SUB MUL DIV ABS LOG
%token EOL
%token POW
%token SQRT
%token COS SIN TAN
%token MOD
%token COMMA
%token <ival> IF THEN ELSE

%right ELSE
%left THEN
%left IF
%left '-' '+'
%left '*' '/' '^'

%%

stmt_list:
        | stmt_list stmt EOL
        ;

stmt:     exp { printf("=%g\n", $1); }
        | VAR STORE exp { variables[$1] = $3; printf("store %g\n", $3); }
        | PRINT exp { printf("true\n");  printf("%lf\n",$2);}
        | if_stmt
        ;

if_stmt:
        IF exp THEN stmt %prec IF
      | IF exp THEN stmt ELSE stmt
      ;

exp: factor
    | exp ADD factor { $$ = $1 + $3; }
    | exp SUB factor { $$ = $1 - $3; }
    | exp POW factor { $$ = pow($1, $3); }
    | SUB factor { $$ = -$2; }
    ;

factor: term
      | factor MUL term { $$ = $1 * $3; }
      | factor DIV term { $$ = $1 / $3; }
      | factor MOD term { $$ = fmod($1, $3); }
      | factor BIGGER term { $$ = $1 > $3 ? 1 : 0; }
      | factor SMALLER term { $$ = $1 < $3 ? 1 : 0; }
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
