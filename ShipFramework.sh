#!/bin/bash
cd $LOCATION
echo "Select a debugging location" 
read $LOCATION
file=$LOCATION
exec 5> $LOCATION
BASH_XTRACEFD="5"
