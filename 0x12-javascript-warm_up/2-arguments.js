#!/usr/bin/node

// print a message depending of the number of arguments passed

const argc = process.argv.length;

if (argc < 3) console.log('No argument')
else if (argc === 3) console.log('Argument found')
else console.log('Arguments found')
