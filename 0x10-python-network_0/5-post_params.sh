#!/bin/bash
#this send a post with arguments
curl -s --request POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
