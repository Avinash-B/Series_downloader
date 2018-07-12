#!/bin/bash

#A Shell program for downloading web series fron index/...............
#Copy your target url here
target_url="http://sv4avadl.uploadt.com/Serial/5CameBack/"
target_quality="480p"
$directory=pwd

for name in $directory/* ;
do
	if [$name="webpage.html"]
	then
		rm webpage.html
	fi
done
curl $target_url -o webpage.html

#Reading every line in webpage.html
python2 downloader.py $target_quality $target_url
