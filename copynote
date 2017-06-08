#!/bin/bash

#define date parameter
d=$(date +%d-%m-%Y)

#make folders, file and define target file
mkdir -p /home/$USER/Documents/clipzor/
touch /home/$USER/Documents/clipzor/xclipDump-$d

NOTE="/home/$USER/Documents/clipzor/xclipDump-$d"

#The clipper
CLIPPER=$(xclip -out -selection c)
echo "#-$CLIPPER" >> $NOTE
