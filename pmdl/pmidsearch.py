#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import argparse
import sys

from pmdl import *
from errors import *
from utils import *


def main():
    print(os.getcwd())
    f_list = str(sys.argv[1])
    PMIDs = []
    with open(f_list) as f:
        for line in f:
            PMIDs.append(line.rstrip())
    links = []
    with open('links.txt', 'a') as fout:
        for id in PMIDs:
            print(id)
            link = get_publisher_links(id)
            print(link)
            fout.write(str(link)+'\n')
    print links





if __name__ == '__main__':
    main()
