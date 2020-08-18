#!/bin/bash
#sends a file in json format
curl -s --request POST "$1" --data @"$2" -H "Content-Type: application/json"
