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
#define MAX_STRING_LEN 49
int flag1=1;

typedef struct {
    char name[MAX_VAR_NAME_LEN];
    int value_int;
    double value_double;
    char value_string[MAX_STRING_LEN];
    int type;//0: int, 1:double, 2: string
} Variable;

Variable variables[MAX_VAR_NUM];
int var_count = 0;
int global_type = 0;//0: int, 1:double, 2: string

%}

%union {
    double num; // �x�s�p��
    char * str;  // �x�s�r��
}

%type <num> exp factor term
%token <num>  NUMBER NUMBER_DOUBLE
%token <str> VAR  
%token <str> STRING
%token STORE END PRINT
%token ADD SUB MUL DIV ABS LOG
%token OUTPUT OUTPUT_OPERATOR NEWLINE EOL 
%token TYPE_INT TYPE_STRING TYPE_DOUBLE 
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
  |calclist IF '(' exp ')' LBRACE OUTPUT output_item END RBRACE EOL
    { 
      if ($4 > 0) { yyparse(); } 
    }
  |calclist if_stmt EOL {}
  |calclist TYPE_STRING VAR STORE STRING END EOL {
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$3) == 0) {
                  strcpy(variables[i].value_string, (char*)$5);
                  variables[i].type = 2;
                  //printf("store %s = %s(%d)\n", variables[i].name, variables[i].value_string, variables[i].type);
                  found = 1;
                  break;
              }
          }
          if (!found) {
              Variable var;
              strcpy(var.value_string, (char*)$5);
              strcpy(var.name, (char*)$3);
              var.type = 2;
              variables[var_count] = var;
              //printf("store %s = %s(%d)\n", variables[var_count].name, variables[var_count].value_string, variables[var_count].type);
              var_count++;
          }    
  }

  |calclist TYPE_INT VAR STORE exp END EOL { 
          //printf("store int\n");
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$3) == 0) {
                  variables[i].value_int = $5;
                  variables[i].type = 0;
                  //printf("store %s = %d(%d)\n", variables[i].name, variables[i].value_int, variables[i].type);
                  found = 1;
                  break;
              }
          }
          if (!found) {
              Variable var;
              var.value_int = $5;
              var.type = 0;
              strcpy(var.name, (char*)$3);
              variables[var_count] = var;
              //printf("store %s = %d(%d)\n", variables[var_count].name, variables[var_count].value_int, variables[var_count].type);
              var_count++;
          }
      }  
  |calclist TYPE_DOUBLE VAR STORE exp END EOL { 
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$3) == 0) {
                  variables[i].value_double = $5;
                  variables[i].type = 1;
                  //printf("store %s = %lf(%d)\n", variables[i].name, variables[i].value_double, variables[i].type);
                  found = 1;
                  break;
              }
          }
          if (!found) {
              Variable var;
              var.value_double = $5;
              var.type = 1;
              strcpy(var.name, (char*)$3);
              variables[var_count] = var;
              //printf("store %s = %lf(%d)\n", variables[var_count].name, variables[var_count].value_double, variables[var_count].type);
              var_count++;
          }
      } 

  |calclist OUTPUT output_item END EOL{}
  ;

output_item:
  |OUTPUT_OPERATOR exp{         
                                    if(flag1!=0){printf ("%g",$2);}flag1=1;
                                }  
  |OUTPUT_OPERATOR VAR{
                                  int found = 0,i;
                                  for (i = 0; i < var_count; i++) {
                                      if (strcmp(variables[i].name, (char*)$2) == 0) {
                                          if(variables[i].type == 0)
                                          {
                                            global_type = 0;
                                            if(flag1!=0){printf("%d",variables[i].value_int);}flag1=1;
                                          }
                                          else if(variables[i].type == 1)
                                          {
                                            global_type = 1;
                                            if(flag1!=0){ printf("%g",variables[i].value_double);}flag1=1;
                                           
                                          }
                                          else if(variables[i].type == 2)
                                          {
                                            global_type = 2;
                                             if(flag1!=0){printf("%s",variables[i].value_string);}flag1=1;
                                            
                                          }
                                          found = 1;
                                          break;
                                      }
                                  }
                                  if (!found) {
                                      printf("Error: %s is not defined\n", $2);
                                  }
                                }
  |OUTPUT_OPERATOR STRING{if(flag1!=0){printf("%s",$2);}flag1=1;}
  |OUTPUT_OPERATOR NEWLINE{if(flag1!=0){printf("\n");}flag1=1; }
  |output_item OUTPUT_OPERATOR VAR{
                                  int found = 0,i;
                                  for (i = 0; i < var_count; i++) {
                                      if (strcmp(variables[i].name, (char*)$3) == 0) {
                                          if(variables[i].type == 0)
                                          {
                                            global_type = 0;
                                            if(flag1!=0){printf("%d",variables[i].value_int);}flag1=1;
                                            
                                          }
                                          else if(variables[i].type == 1)
                                          {
                                            global_type = 1;
                                            if(flag1!=0){ printf("%g",variables[i].value_double);}flag1=1;
                                           
                                          }
                                          else if(variables[i].type == 2)
                                          {
                                            global_type = 2;
                                            if(flag1!=0){ printf("%s",variables[i].value_string);}flag1=1;
                                           
                                          }
                                          found = 1;
                                          break;
                                      }
                                  }
                                  if (!found) {
                                      printf("Error: %s is not defined\n", $3);
                                  }
                                }
  |output_item OUTPUT_OPERATOR exp{ if(flag1!=0){ printf("%g",$3);}flag1=1; }
  |output_item OUTPUT_OPERATOR STRING{ if(flag1!=0){ printf ("%s",$3);}flag1=1; }
  |output_item OUTPUT_OPERATOR NEWLINE{ if(flag1!=0){ printf ("\n");}flag1=1; }
  ;
if_stmt:
  IF '(' exp ')' LBRACE calclist RBRACE
    {  }
  | IF '(' exp ')' LBRACE calclist RBRACE ELSE LBRACE calclist RBRACE
    {  }
    
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
  | factor BIGGER term {if($1 > $3){$$=1;flag1=1;}else{$$=0;flag1=0;} }
  | factor SMALLER term { if($1 < $3){$$=1;flag1=1;}else{$$=0;flag1=0;} }
  | factor BIGEQUAL term { if($1 > $3||$1==$3){$$=1;flag1=1;}else{$$=0;flag1=0;} }
  | factor SMALLEQUAL term { if($1 < $3||$1==$3){$$=1;flag1=1;}else{$$=0;flag1=0;}}
  | factor EQUAL term {if($1 == $3){$$=1;flag1=1;}else{$$=0;flag1=0;} }
  ;
  
term:NUMBER {$$=$1; if($1==0){flag1=0;}}
  |NUMBER_DOUBLE {$$=$1; if($1==0){flag1=0;}}
  |VAR { 
          int found = 0,i;
          for (i = 0; i < var_count; i++) {
              if (strcmp(variables[i].name, (char*)$1) == 0) {
                  if(variables[i].type == 0)
                  {
                    global_type = 0;
                    $$ = variables[i].value_int;
                  }
                  else if(variables[i].type == 1)
                  {
                    global_type = 1;
                    $$ = variables[i].value_double;
                  }

                  found = 1;
                  break;
              }
          }
          if (!found) {
              printf("variable %s not found\n", (char*)$1);
          }
      }
  |LOG term {$$ = log10($2);}
  |ABS exp ABS {$$=$2>=0?$2:-$2;}
  | SQRT '(' exp ')' { $$ = sqrt($3); }
  | COS '(' exp ')' { $$ = cos($3); }
  | SIN '(' exp ')' { $$ = sin($3); }
  | TAN '(' exp ')' { $$ = tan($3); }

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
