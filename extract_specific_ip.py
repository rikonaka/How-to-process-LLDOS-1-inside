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

filename = 'res_gai'

def is_same(index, ip):
	ip_none = ip.strip().split(".")
	index_none = index.strip().split(".")
	ip_ch = ''.join(ip_none)
	index_ch = ''.join(index_none)
	if ip_ch == index_ch:
		return True
	else:
		return False


def get_res():
	ip_list = ['172.16.112.50'] # Put the ip which you want extract
	
	XX_list = ['-1', '-2']
	for XX in XX_list:
		for ip in ip_list:
			co = open(filename, 'r')
			for ge in co.readlines():
				ge_l = ge.split(",")
				get_t = ge_l[int(XX)]
				print 'get_t', get_t
				get_f = str(get_t)
				some = is_same(get_f, ip)
				if some:
					some_save = open('%s' % ip, 'a')
					ge_f = judge_last(ge)
					some_save.writelines(ge_f)
					some_save.close()
			co.close()

def judge_last(line):
	line_split = line.strip().split(",")
	last_of_line = line_split[-1]
	search_last = re.search(r'\.', last_of_line)
	if search_last == None:
		re_tu_1 = line_split[0:-1]
		re_tu_2 = ','.join(re_tu_1)
		re_tu = re_tu_2 + '\n'
		return re_tu
	else:
		return line

def main():
	get_res()

if __name__ == '__main__':
	main()
