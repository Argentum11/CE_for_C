cd ..
flex CFE.l
bison -d CFE.y
gcc CFE.tab.c lex.yy.c -lfl
cd test
pytest -rp --md-report --md-report-color=auto --md-report-tee --md-report-output=report.md
python format_report.py
del input.txt
del result.txt
pause
