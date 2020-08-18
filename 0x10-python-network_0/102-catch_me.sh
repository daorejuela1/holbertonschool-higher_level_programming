#!/bin/bash
# follow pattern to catch result
 curl -sL --request PUT 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin: HolbertonSchool"
