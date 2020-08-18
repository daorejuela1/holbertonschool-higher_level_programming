#!/bin/bash
#checks url content
curl -sI "$1" | grep Length | cut -d ' ' -f2
