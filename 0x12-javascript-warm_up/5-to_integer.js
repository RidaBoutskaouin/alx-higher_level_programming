#!/usr/bin/node
// Script that prints My number: <first argument converted in integer>

isNaN(process.argv[2]) ? console.log('Not a number') : console.log('My number: ' + parseInt(process.argv[2]));
