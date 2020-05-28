@ECHO OFF
:: This batch file reveals OS, hardware, and networking configuration.
TITLE ELK Initialization

set EPATH=D:\Programming\elasticsearch-7.7.0\bin
set LPATH=D:\Programming\logstash-7.7.0\bin
set KPATH=D:\Programming\kibana-7.7.0-windows-x86_64\bin

:: Start Elasticsearch Cluster On Console
call %EPATH%\elasticsearch.bat -Ecluster.name=escluster -Enode.name=node-1

:: Start 2nd Node using another console
call %EPATH%\elasticsearch.bat -Ecluster.name=escluster -Enode.name=node-2 -Epath.data=data2 -Epath.logs=log2

:: Start 3rd Node using 3rd console
call %EPATH%\elasticsearch.bat -Ecluster.name=escluster -Enode.name=node-3 -Epath.data=data3 -Epath.logs=log3

call %LPATH%\logstash.bat -e "input { stdin { } } output { stdout {} }"

call %KPATH%\kibana.bat
PAUSE