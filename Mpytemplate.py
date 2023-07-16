#!/usr/bin/env python
'Template for a madagascar python program'

##   Copyright (C) 2010 University of Texas at Austin
##  
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2 of the License, or
##   (at your option) any later version.
##  
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
##  
##   You should have received a copy of the GNU General Public License
##   along with this program; if not, write to the Free Software
##   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import sys

"""
Convert txt file into asc readable by sfdd program
    pytemplate <output.asc> <column>
Usage:
    - Generate a txt file with 'echo -e "1 2 3\n4 5 6" > file.txt
    - Convert to asc with '<file.txt pytemplate output.asc 1 > output.asc'
    - Convert to RSF file using sfdd 'sfdd <output.asc form=native type=float'
"""

data = sys.stdin.readlines()
i = int(sys.argv[2])-1

for line in data:
	string=line.strip()
	col = string.split()[i]
	sys.stdout.write(col+' ')

sys.stdout.write("n1="+str(len(data))+" d1=1 o1=0  n2=1 d2=1 o2=0 data_format=ascii_float in="+sys.argv[1])
