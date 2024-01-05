#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the response
# A variable is created with the value of the second argument

curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD" -L
