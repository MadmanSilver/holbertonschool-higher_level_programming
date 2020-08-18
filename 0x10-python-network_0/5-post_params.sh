#!/bin/bash
# send post variables and display
curl -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
