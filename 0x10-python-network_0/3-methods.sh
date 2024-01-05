#!/bin/bash
# script to display the allowed HTTP methods the server will accept.
curl -sI "$1" | grep Allow | cut -d' ' -f2-
