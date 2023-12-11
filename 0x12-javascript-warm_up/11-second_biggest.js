#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

process.argv.length <= 3 ? console.log(0) : console.log(process.argv.sort((a, b) => a - b)[process.argv.length - 2]);
