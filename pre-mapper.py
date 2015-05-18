#!/usr/bin/python

import sys
from random import randint

sys.stderr.write("Started mapper.\n");
subject = "god"
max_timestamp = 24*7

def main(argv):
    for line in sys.stdin:
        try:
            if line.startswith("@") and line.find(subject)!=-1:
                print line.rstrip()+"#######"+str(randint(0,max_timestamp))
        except Exception, e:
            continue

if __name__ == "__main__":
    main(sys.argv)