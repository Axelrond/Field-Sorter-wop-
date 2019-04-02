import string
import random
import winsound
import sys
import math
import os

winsound.Beep(300,200)

filelist = open("info.txt", "r")
print (filelist)
filelist.read() # reads the entire file
splitlist = list()

class data:
    def __init__(self, artist, title, album, track, year, genre):
        self.artist = artist
        self.title = title
        self.album = album
        self.track = track
        self.year = year
        self.genre = genre

for line in filelist:
    filelist = list.split(', ')
    splitlist.append(filelist)

for column in splitlist:
    if (len(column) > 1): #to skip the first line
        artist = column[0].strip()
        title = column[1].strip()
        album = column[2].strip()
        track = column[3].strip()
        year = column[4].strip()
        genre = column[5].strip()



rows = []
for line in open("info.txt"):
    line = line.split()
    if len(line) != 6:
        continue

    artist, title, album, track, year, genre = line

    # Add them in the order you want to sort by
    rows.append((album, title, artist, track, year, genre)) 

rows.sort()

print (line)
