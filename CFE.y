%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "CFE.tab.h"
#include <ctype.h>

double variables[256];
int flag1;

void yyerror(const char *s);

%}

%union {
    double dval;
    char sval;
    int ival;
    int is_print;
    struct {
        int condition;
        double value;
    } if_stmt_type;
}


%type <dval> exp factor term
%type <is_print> stmt
%type <if_stmt_type> if_stmt
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
%nonassoc IF
%nonassoc THEN
%nonassoc ELSE

%left '-' '+'
%left '*' '/' '^'

%%

stmt_list:
        | stmt_list stmt EOL
        ;

stmt:     exp { $$ = 0; }
        | VAR STORE exp { variables[$1] = $3; printf("store %g\n", $3); $$ = 0; }
        | if_stmt {printf("in condition %d\n",$1.condition) if ($1.condition) { printf("in condition 1 true %d\n",flag1);flag1 = 1; } else { printf("false\n"); flag1 = 0;} $$ = 0; }
        | PRINT exp { printf("in print flag : %d\n",flag1); if(flag1==1) {printf("%lf\n",$2); $$ = 1; }}
       
        ;

if_stmt:
          IF exp THEN stmt { $$.condition = $2 > 0; printf("in $2 flag : %d\n",$2); if ($2 > 0) { if ($4 == 1) { printf("in is true\n"); flag1 = 1;} } else { printf("false\n");flag1 = 0; } }
        | IF exp THEN stmt %prec ELSE ELSE stmt { $$.condition = $2 > 0; if ($2 > 0) { if ($4 == 1) { printf("true\n" );flag1 = 1; } } else { if ($6 == 1) { printf("false\n");flag1 = 0; } } }
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
