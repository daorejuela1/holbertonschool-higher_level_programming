#!/bin/bash
# creates a new line
curl -sI "$1" | grep Allow | cut -d ":" -f2| xargs
