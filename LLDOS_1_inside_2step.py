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
# -*- coding: utf-8 -*-
import os
import sys
import re

filename = 'result-alert_i'

def first_thing():
	get_o = open(filename, 'r')
	save_o = open('result_1', 'a')
	for g in get_o.readlines():
		g_1 = re.sub(r'\[', '', g)
		g_2 = re.sub(r'\]', '', g_1)
		save_o.writelines(g_2)
	get_o.close()
	save_o.close()

def find_classification():
	cla = open('result_1', 'r')
	s_cla = open('1', 'a')
	for nn in cla.readlines():
		i = nn.split(",")
		uu = []
		date = i[0:2]
		for d in date:
			uu.append(d)
		get_classification = 0
		for get in i:
			if get.strip() == 'Classification':
				break
			else:
				get_classification += 1
		if get_classification > 9:
			uu.append(i[-7])
			uu.append('None')
		else:
			cla_up = i[get_classification - 1]
			uu.append(cla_up)
			cla_down = i[get_classification + 1]
			uu.append(cla_down)
		ignore_first = True
		for find in i:
			f = re.findall('\d+.\d+.\d+.\d+', find)
			for f_1 in f:
				if ignore_first:
					ignore_first = False
				else:
					uu.append(f_1)
		fin = ",".join(uu)
		s_cla.writelines(fin)
		s_cla.writelines("\n")
	s_cla.close()
	cla.close()


def sub_word():
	sub_w = open('1', 'r')
	save_sub = open('re', 'a')
	for i in sub_w:
		r_t = re.sub(r'\]', '', i)
		save_sub.writelines(r_t)
	sub_w.close()
	save_sub.close()

def re_build():
	k_open = open('re', 'r')
	k_save = open('res_gai', 'a')
	for k in k_open:
		little = re.sub(r'\-', ' ', k)
		mid = re.sub(r'\/', ',', little)
		k_save.writelines(mid)
	k_open.close()
	k_save.close()

def remove_last_3():
	last_fp = open('res_gai', 'r')
	last_sa = open('final', 'a')
	ko = []
	show = 1
	for i in last_fp.readlines():
		i_split = i.split(",")
		print show
		for num in range(0, 8):
			if num == 5:
				print 'no'
			else:
				ko.append(i_split[num])
		w_k = ','.join(ko)
		last_sa.writelines(w_k)
		show += 1

def remove_l():
	os.remove('1')
	os.remove('result_1')
	os.remove('re')


def main():
	first_thing()
	find_classification()
	sub_word()
	re_build()
	#remove_last_3()
	remove_l()

if __name__ == '__main__':
	main()
