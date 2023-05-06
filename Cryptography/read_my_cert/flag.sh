#!/bin/bash

openssl req -in readmycert.csr -text | grep -oE "picoCTF{.*?}"