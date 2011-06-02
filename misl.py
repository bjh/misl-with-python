#!/usr/bin/env python

from misl.action_man import ActionMan
import argparse

parser = argparse.ArgumentParser(description='do it to it')
parser.add_argument('--dry', action='store_true', default=False)
parser.add_argument('-p', '--path', default=None, action='store', dest='path', help='the directory containg the albums/directories to process', required=True)

try:
    args = parser.parse_args()        
    action = ActionMan(args.path)

    if args.dry:
        action.dry_run()
    else:
        action.run()

except KeyboardInterrupt:
    print
    print
    print '-' * 30
    print "caught CTRL-C, bye...bye"
    print '-' * 30
    exit()

