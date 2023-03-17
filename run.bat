flex CFE.l
bison -d CFE.y
gcc CFE.tab.c lex.yy.c -lfl
a.exe
pause