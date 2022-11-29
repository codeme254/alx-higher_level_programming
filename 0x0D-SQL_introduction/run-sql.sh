#!/usr/bin/env bash

# My bash script for running sql files without having to type the long commands
# usage: ./run-sql.sh filename
# If you want to use this script, change zaphdev part to your sql username
cat $1 | mysql -hlocalhost -uzaphdev -p

