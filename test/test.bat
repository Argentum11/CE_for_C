cd ..
flex CFE.l
bison -d CFE.y
gcc CFE.tab.c lex.yy.c -lfl
cd test
FOR /R %%I in (*.txt) DO ..\a.exe < %%I
pause