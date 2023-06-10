flex CE.l
bison -d CE.y
gcc CE.tab.c lex.yy.c -lfl
a.exe
pause