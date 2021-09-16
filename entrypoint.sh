#!/bin/bash

echo "APP RUNNING";

echo "READING IEXEC ARGS";
args=$@
echo $args;

mkdir /tmp/iexec_in
mkdir /tmp/iexec_out

echo 'READING IEXEC RUNTIME VARIABLES';

FILE1=$args
echo $FILE1

echo "start program"

python app/app.py $FILE1
echo "end program" 
echo "CREATING determinism.txt IN /iexec_out/";
echo "ok" > /iexec_out/determinism.txt && echo "done";
echo "{ \"deterministic-output-path\" : \"/iexec_out/determinism.txt\" }" > /iexec_out/computed.json
echo "OUTPUT DIRECTORY FINAL CONTENT";
ls -a /iexec_out;
echo "FINISH";
