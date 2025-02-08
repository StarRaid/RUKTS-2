@ECHO OFF

:start
python nml/nmlc testing.nml -o RUKTS2.grf -s

PAUSE
goto start
