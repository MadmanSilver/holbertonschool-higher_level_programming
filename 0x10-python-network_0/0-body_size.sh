#!/bin/bash
# use curl to display size of response
curl -s "$1" | wc -c
