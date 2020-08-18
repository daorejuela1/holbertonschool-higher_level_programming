#!/bin/bash
#Added write option to get status code
curl -sw "%{http_code}" "$1" -o /dev/null
