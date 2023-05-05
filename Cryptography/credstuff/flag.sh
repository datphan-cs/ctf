#!/bin/bash

line_num=`grep -n -i "cultiris" usernames.txt | cut -f1 -d ":"`
flag=`sed "${line_num}!d" passwords.txt`
echo $flag | tr '[A-Z]' '[N-ZA-M]' | tr '[a-z]' '[n-za-m]'