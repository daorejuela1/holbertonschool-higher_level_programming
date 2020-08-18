#!/bin/bash
#prints content if 200 is in valu
#prints content if 200 is in valuee
condition=$(curl -sLI "$1" | grep "200 OK" | cut -d " " -f2)
if [[ $condition == 200 ]]
then
	curl -sL "$1"
fi
