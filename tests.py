#!/usr/bin/env python
import fnmatch
from os import walk, path
from sys import exit, stdout
import eyeD3
import argparse


tag = eyeD3.Tag()
tag.link("/Volumes/music/film-scores/Armando Sciascia - Mondi Caldi di Notte/18 Ballata Messicana.mp3")
#tag.link("/Volumes/music/film-scores/Armando Sciascia - Mondi Caldi di Notte/19 Incontro Inatteso.mp3")

print tag.getArtist()
print tag.getAlbum()
print tag.getTitle()
print '-' * 70

for frame in tag.frames:
    print frame

print dir(tag)

exit()
