%{
#include <stdio.h>
#include <math.h>
typedef struct {
  int value;
  char* name;
} myVar;
%}

%token NUMBER VAR
%token STORE END PRINT
%token ADD SUB MUL DIV ABS LOG
%token EOL
%token POW
%token SQRT
%token MOD
%left '-' '+'
%left '*' '/'

%%


calclist:
  |calclist VAR STORE exp END EOL{printf ("store %d\n",$4);}
  |calclist exp EOL{printf ("=%d\n",$2);}
  |calclist PRINT exp EOL{printf ("%d\n",$3);}
  ;
  
exp:factor {$$ = $1;}
  |exp ADD factor{$$=$1+$3;}
  |exp SUB factor{$$=$1-$3;}
  |SUB factor{$$=-$2;}
  ;

factor:term {$$=$1;}
  |factor MUL term{$$=$1*$3;}
  |factor DIV term{$$=$1/$3;}
  |factor MOD term{$$=$1%$3;}
  ;

term:NUMBER {$$=$1;}
  |LOG term {$$ = log($2);}
  |ABS exp ABS {$$=$2>=0?$2:-$2;}
  |POW term{$$=pow($1,$2);}
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
