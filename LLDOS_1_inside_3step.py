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

filename = 'res_gai++save++'

def is_same(index):
	# if same return 0
	# if not same return the number of location in the list
	file_count = 1
	same_j = True
	file_same = open('same', 'r')
	for i in file_same.readline():
		if len(i) != 0:
			for i in file_same:
				i_none = i.strip().split(".")
				index_none = index.strip().split(".")
				i_ch = ''.join(i_none)
				index_ch = ''.join(index_none)
				if i_ch == index_ch:
					return file_count
				else:
					file_count += 1
	file_same.close()
	file_same = open('same', 'a')
	file_same.writelines(index)
	#file_same.writelines('\n') # This is necessary if you get the last of line
	file_same.close()
	return file_count

def first_use_fanction(index_1):
	fu = open('same', 'a')
	index_2 = index_1.strip('\n')
	fu.writelines(index_2)
	fu.write('\n')
	fu.close()

def get_res():
	co = open(filename, 'r')
	first_use = True
	for ge in co.readlines():
		ge_l = ge.split(",")
		get_t = ge_l[-1]
		get_f = str(get_t)
		if first_use:
			first_use_fanction(get_f)
			first_use = False
		else:
			some = is_same(get_f)
			if some:
				some_save = open('temp_%d.txt' % some, 'a')
				some_save.writelines(ge)
				some_save.close()
	co.close()

def merge_file():
	file_nn = 1
	super_result = open('super', 'a')
	while True:
		if os.path.isfile('temp_%d.txt' % file_nn):
			just_open = open('temp_%d.txt' % file_nn, 'r')
			print '%d ...' % file_nn
			s_list = []
			for jo in just_open.readlines():
				jo_1 = jo.strip('\n').split(",")
				for j in jo_1:
					s_list.append(j)
			s_save = ','.join(s_list)
			super_result.writelines(s_save)
			super_result.writelines('\n')
			just_open.close()
			file_nn += 1
		else:
			break
	super_result.close()


def main():
	get_res()
	merge_file()

if __name__ == '__main__':
	main()
