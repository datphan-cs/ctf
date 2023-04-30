#!/usr/bin/bash

cat flag.txt | tr -d '\n' |  rev | tr -d "'" | cut -d "\\" -f 1