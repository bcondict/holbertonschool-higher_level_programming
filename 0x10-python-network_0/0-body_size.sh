#!/usr/bin/bash
# takes in a URL, sends a request to that URL and displays the size of the body 

curl -sI '$1' | grep 'Content-Lenght' | cut -d' ' -f 2
