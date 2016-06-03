#
# 
# Copyright 2016 isinstance <super_big_hero@sina.com>/*
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# 
#

#!/usr/bin/env python

import os
import re

filename = '172.16.112.50' # input you filename after the LLDOS_1_inside_3step.py

def space_to_some(one):
	yu = re.sub(r' ', ',', one)
	return str(yu)

def space_new():
	fp = open(filename, 'r')
	fp_save = open(filename + '+result', 'a')
	for i in fp.readlines():
		wt = []
		i_1 = i.split(",")
		get_2 = i_1[1]
		get_some = space_to_some(get_2)
		wt.append(i_1[0])
		get_some_0 = get_some.split(",")[0]
		get_some_1 = get_some.split(",")[1]
		wt.append(get_some_0)
		wt.append(get_some_1)
		wt.append(i_1[2])
		wt.append(i_1[3])
		ww = ",".join(wt)
		fp_save.writelines(ww)
		fp_save.writelines('\n')
	fp.close()
	fp_save.close()

def add_time():
	ad_fp = open(filename + '+result', 'r')
	ad_save = open(filename + '+final', 'a')
	for i in ad_fp.readlines():
		i_1 = i.split(",")
		count_num = 0
		op = []
		for ii in range(0, 8):
			if ii == 0:
				ii_0 = i_1[ii]
				op.append(ii_0)
			elif ii == 1:
				ii_1 = i_1[ii]
				op.append(ii_1)
			elif ii == 2:
				ii_2 = i_1[ii]
				op.append(ii_2)
			elif ii == 3:
				ii_3 = i_1[ii]
				op.append(ii_3)
			else:
				op.append(i_1[ii])
		print op
		op_w = ",".join(op)
		ad_save.writelines(op_w)
	ad_fp.close()
	ad_save.close()

def delete_source():
	de_fp = open(filename + '+final', 'r')
	de_save = open(filename + '+delete', 'a')
	for i in de_fp.readlines():
		i_1 = i.split(",")
		pop_num = 0
		for find in i_1:
			if find.strip('\n') == filename:
				i_1.pop(pop_num)
			else:
				pop_num += 1
		i_2 = ",".join(i_1)
		de_save.writelines(i_2)
		#de_save.writelines('\n') # keep this
	de_fp.close()
	de_save.close()

def main():
	space_new()

if __name__ == "__main__":
	main()
