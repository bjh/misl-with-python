#!/usr/bin/env python
import fnmatch
from os import walk, path
from sys import exit, stdout
#import eyeD3
import tags
#import argparse

#parser = argparse.ArgumentParser(description='do it to it')
#parser.add_argument('--dry', action='store_true', default=False)
#parser.add_argument('-p', '--path', default=None, action='store', dest='path', help='the directory containg the albums/directories to process', required=True)

class ActionMan(object):
	def __init__(self, directory):
		self.d = directory
		self.tags = tags.Tags()
		self.logging = True

	def log(self, message):
		if self.logging:
			print message

	def find_covers(self, filenames):
		'''
		collect all the images in the list of filenames
		'''
		#self.log('find_covers')
		image_exts = ['.jpg', '.gif', '.png', '.bmp', '.jpeg']

		covers = []
		for name in filenames:
			basename, extension = path.splitext(name)
			if extension in image_exts:
				covers.append(name)
		#self.log('covers %s' % covers)
		return covers

	def valid_choice(self, choice):
		return choice.isdigit()

	def ask(self, covers):
		'''
		ask which image to use for the cover image
		'''
		#self.log('ask')
		stdout.write('\a')
		stdout.flush()
		
		print
		print "which cover to use for this album?"
		count = 0
		for cover in covers:
			print "[%s] %s\n" % (count, cover)
			count += 1
		# get users choice
		choice = raw_input("input the cover #: ")
	
		if self.valid_choice(choice):
			return choice
		else:
			self.ask(covers)
		

	def choose_cover(self, covers):
		'''
		if there is only one image, use it
		otherwise ask which image to use as the cover
		'''
		#self.log('choose_cover')
		if len(covers) <= 0:
			self.log('no covers for this album')
			return
		elif len(covers) > 1:
			idx = int(self.ask(covers))
			self.log('idx is %s' % idx)
			return covers[idx]
		else:
			#self.log('only one image found, using it as the cover image')
			return covers[0]

	def is_mp3(self, filename):
		basename, extension = path.splitext(filename)
		return extension.lower() == '.mp3'

	def is_album(self, filenames):
		#self.log('is_album') 
		for name in filenames:
			# basename, extension = path.splitext(name)
			# if extension == '.mp3':
			if self.is_mp3(name):
				#self.log('YES I AM AN ALBUM!')
				return True
		return False

	def add_cover_to_mp3s(self, cover, directory, filenames):
		'''
		add the selected image as a front cover image in the ID3 tags
		'''
		#self.log('add_cover_to_mp3s % s' % cover)
		filenames.sort()
		for name in filenames:
			if self.is_mp3(name):
				self.tags.update_image(cover, directory, name)
				

	def dry_run(self):
		'''
		just run through the directories printing which ones
		this app thinks are albums
		'''
		for dirname, dirnames, filenames in walk(self.d):
			if self.is_album(filenames):
				print "ALBUM: %s" % path.basename(dirname)

	def run(self):
		'''
		this is where the magic happens...
		'''
		for dirname, dirnames, filenames in walk(self.d):
			print '-' * 70
			print "processing album: %s" % dirname
			cover = self.choose_cover(self.find_covers(filenames))
			
			if cover:
				self.add_cover_to_mp3s(cover, dirname, filenames)
>>>>>>> b1bae5682e1d098a7b4b530e7f7d07c3f5a3e290


#if __name__ == '__main__':

