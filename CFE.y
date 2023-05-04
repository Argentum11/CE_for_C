%{
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_VAR_NUM 100
#define MAX_VAR_NAME_LEN 30

typedef struct {
    char name[MAX_VAR_NAME_LEN];
    int value;
} Variable;

Variable variables[MAX_VAR_NUM];
int var_count = 0;

%}

%token  NUMBER VAR STRING
%token STORE END PRINT
%token ADD SUB MUL DIV ABS LOG
%token OUTPUT OUTPUT_OPERATOR NEWLINE EOL 

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
  |calclist OUTPUT output_item END EOL{}
  ;

output_item:OUTPUT_OPERATOR exp{printf ("%d",$2);}
  |OUTPUT_OPERATOR STRING{printf ("%s",$2);}
  |OUTPUT_OPERATOR NEWLINE{printf ("\n");}
  |output_item OUTPUT_OPERATOR exp{printf ("%d",$3);}
  |output_item OUTPUT_OPERATOR STRING{printf ("%s",$3);}
  |output_item OUTPUT_OPERATOR NEWLINE{printf ("\n");}
  ;

exp:factor {$$ = $1;}
  |exp ADD factor{$$=$1+$3;}
  |exp SUB factor{$$=$1-$3;}
  |SUB factor{$$=-$2;}
  ;

factor:term {$$=$1;}
  |factor MUL term{$$=$1*$3;}
  |factor DIV term{$$=$1/$3;}
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
